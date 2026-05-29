import re
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

POSITIVE_WORDS = {
    "amazing", "brilliant", "outstanding", "excellent", "wonderful", "fantastic",
    "superb", "masterpiece", "breathtaking", "stunning", "perfect", "incredible",
    "beautiful", "enjoyable", "great", "best", "awesome", "magnificent", "hilarious",
    "touching", "emotional", "gripping", "captivating", "flawless", "loved",
    "impressive", "remarkable", "extraordinary", "genius", "powerful", "moving",
    "inspiring", "thrilling", "enchanting", "delightful", "heartwarming",
    "unforgettable", "spectacular", "phenomenal", "glorious", "splendid",
    "terrific", "marvelous", "exceptional", "engaging", "riveting", "creative",
    "refreshing", "compelling", "vivid", "good", "nice", "fine", "decent", "solid",
    "worthy", "pleasant", "fun", "cool", "liked", "interesting", "fascinating",
    "charming", "warm", "clever", "smart", "rich", "deep", "exciting", "entertaining",
    "satisfying", "rewarding", "well", "better"
}

NEGATIVE_WORDS = {
    "boring", "terrible", "awful", "worst", "bad", "disappointing", "dull",
    "horrible", "waste", "poor", "pathetic", "stupid", "ridiculous", "slow",
    "ugly", "unwatchable", "annoying", "predictable", "forgettable", "offensive",
    "mediocre", "bland", "flat", "weak", "mess", "disaster", "failure", "pointless",
    "lifeless", "tedious", "overrated", "confusing", "incoherent", "uninspired",
    "derivative", "shallow", "unconvincing", "forced", "cringe", "laughable",
    "atrocious", "abysmal", "dreadful", "insufferable", "pretentious", "hollow",
    "soulless", "worse", "fail", "hate", "hated", "dislike", "silly"
}

NEGATIONS = {"not", "never", "no", "neither", "nor", "barely", "hardly", "doesn't", "isn't", "wasn't", "won't", "can't", "couldn't", "didn't"}
INTENSIFIERS = {"very", "extremely", "absolutely", "incredibly", "truly", "deeply", "utterly", "completely", "totally", "highly", "super", "really"}

def analyze_sentiment_logic(text):
    text = text.lower()
    # List of common contrast words
    CONTRAST_WORDS = {"but", "however", "though", "although", "yet", "nevertheless"}
    
    # Split by contrast words to identify shifts in sentiment
    # We use a regex that keeps the delimiter so we know where segments split
    segments = re.split(r'(\b(?:but|however|though|although|yet|nevertheless)\b)', text)
    
    overall_pos_score = 0.0
    overall_neg_score = 0.0
    pos_found = []
    neg_found = []

    for i, segment in enumerate(segments):
        # We give slightly more weight to segments that appear after a contrast word
        # "It was okay, but the ending was poor" -> the second part is usually the final verdict
        weight = 1.3 if i > 0 else 1.0
        
        words = re.findall(r'\b\w+\b', segment)
        for j, word in enumerate(words):
            prev_word = words[j-1] if j > 0 else ""
            multiplier = 1.5 if prev_word in INTENSIFIERS else 1.0
            negated = prev_word in NEGATIONS

            if word in POSITIVE_WORDS:
                if negated:
                    overall_neg_score += multiplier * weight
                    neg_found.append(f"not {word}")
                else:
                    overall_pos_score += multiplier * weight
                    pos_found.append(word)
            elif word in NEGATIVE_WORDS:
                if negated:
                    overall_pos_score += multiplier * weight
                    pos_found.append(f"not {word}")
                else:
                    overall_neg_score += multiplier * weight
                    neg_found.append(word)

    total = overall_pos_score + overall_neg_score
    diff = abs(overall_pos_score - overall_neg_score)

    # Decision Logic for Sentiment
    if total == 0:
        sentiment = "neutral"
        confidence = 50
    # If both types of words are present and their scores are close, it's neutral (mixed)
    elif overall_pos_score > 0 and overall_neg_score > 0 and diff <= 1.5:
        sentiment = "neutral"
        confidence = 65 + (total * 2) 
    else:
        if overall_pos_score > overall_neg_score:
            sentiment = "positive"
            confidence = 60 + (overall_pos_score / (total + 0.1) * 35)
        else:
            sentiment = "negative"
            confidence = 60 + (overall_neg_score / (total + 0.1) * 35)

    confidence = round(max(40, min(99, confidence)), 1)
    pos_found = list(dict.fromkeys(pos_found))[:5]
    neg_found = list(dict.fromkeys(neg_found))[:5]

    # AI Explanation
    if sentiment == "neutral":
        if overall_pos_score > 0 and overall_neg_score > 0:
            explanation = f"Balanced Feedback: We detected positive signals like '{', '.join(pos_found[:2])}' but also critical points like '{', '.join(neg_found[:2])}', resulting in a mixed neutral tone."
        else:
            explanation = "Objective Tone: The review focuses on descriptive details without strong emotional markers, placing it in the neutral category."
    elif sentiment == "positive":
        explanation = f"Positive Vibe: The strengths ({', '.join(pos_found[:3])}) clearly outweigh any concerns, indicating an enjoyable experience."
    else:
        explanation = f"Critical Tone: The analysis found significant negative indicators like '{', '.join(neg_found[:3])}', which dominate the feedback."

    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "positive_words": pos_found,
        "negative_words": neg_found,
        "explanation": explanation
    }

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'review' not in data:
        return jsonify({"error": "No review text provided"}), 400
    
    result = analyze_sentiment_logic(data['review'])
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
