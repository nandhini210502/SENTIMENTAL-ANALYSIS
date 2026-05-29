# 🎬 CineScope AI — Movie Review Sentiment Analyzer

CineScope AI is a premium, high-performance web application designed to analyze the emotional tone of movie reviews. Originally evolved from an API-dependent system, it has been refactored into a **zero-dependency, decoupled architecture** that utilizes a robust rule-based sentiment engine and sophisticated CSS-animated reaction scenes.

---

## 📖 Project Overview

The primary goal of CineScope AI is to provide instant, transparent, and visually engaging sentiment analysis for film criticism. Unlike generic analyzers, CineScope is specifically tuned for the nuances of movie reviews, handling complex sentence structures, negations, and emotional shifts.

The project features a **Dual-Mode Architecture**:
1.  **Standalone Mode**: A pure "Single-File" experience (`cinescope_ai.html` or the frontend folder) where analysis happens entirely in the browser using localized JavaScript logic.
2.  **System Mode**: A decoupled architecture with a **Python Flask Backend** for scalable API-based analysis.

---

## ✨ Key Features

### 🧠 Intelligent Sentiment Engine
-   **Tri-Class Classification**: Categorizes reviews into **Positive**, **Negative**, or **Neutral**.
-   **Weighted Segment Analysis**: Understands contrast words like *but*, *however*, and *yet* to weigh the "final verdict" of a review more heavily.
-   **Negation Handling**: Accurately flips sentiment when words like *not*, *never*, or *didn't* are used (e.g., "not good" is detected as negative).
-   **Intensifier Boosting**: Detects emphasis from words like *extremely*, *absolutely*, and *really* to adjust confidence scores.

### 🎨 Premium UI/UX
-   **Glassmorphism Dashboard**: A modern, translucent design with vibrant gradients and subtle micros-interactions.
-   **Sentiment Vibe Visualizer**: Replaces external GIFs with high-performance, **Pure CSS/SVG Reaction Scenes** (😄, 😢, 🤔) that respond dynamically to the analysis.
-   **Real-time Highlighting**: Automatically scans the review and highlights positive (green) and negative (red) trigger words.
-   **Interactive Data Visualization**:
    *   **Doughnut Chart**: Real-time distribution of all analyzed sentiments.
    *   **Bar Chart**: Historical trend tracking of prediction confidence.

### 🛠️ Comprehensive Functionality
-   **Dark/Light Mode**: Full theme support with smooth transitions.
-   **History Log**: Persistent session history showing the last 20 analyzed reviews.
-   **Confidence Meter**: A visual representation of how certain the AI is about its prediction.
-   **AI Explanation**: Generates a human-readable summary explaining *why* a certain sentiment was chosen.

---

## 📂 Project Structure

```text
SENTIMENTAL-ANALYSIS/
├── cinescope/
│   ├── backend/
│   │   └── app.py            # Flask Server & Rule-based NLP Engine
│   ├── frontend/
│   │   ├── index.html        # Main Interactive Dashboard (Pure JS Mode)
│   │   └── public/
│   │       └── gifs/         # (Optional) Fallback assets
│   └── requirements.txt      # Backend Dependencies (Flask, Flask-CORS)
├── cinescope_ai.html         # Standalone All-in-One Version
├── giphy.gif                 # Branding Asset
└── README.md                 # Project Documentation (Current)
```

---

## 🚀 Installation & Execution

### 🔹 Option 1: Standalone Frontend (Recommended for quick use)
1.  Navigate to `cinescope/frontend/index.html` or uses the root `cinescope_ai.html`.
2.  Open the file in any modern web browser.
3.  **No installation required.**

### 🔹 Option 2: Full-Stack (Backend API)
1.  **Requirement**: Ensure Python 3.8+ is installed.
2.  **Install Dependencies**:
    ```bash
    cd cinescope
    pip install -r requirements.txt
    ```
3.  **Run the Server**:
    ```bash
    cd backend
    python app.py
    ```
    The server will start on `http://localhost:5000`.
4.  **API Usage**:
    -   **Endpoint**: `POST /analyze`
    -   **Payload**: `{ "review": "The movie was amazing!" }`
    -   **Response**: Returns sentiment, confidence, positive/negative words, and an explanation.

---

## 🔍 Technical Implementation

### The NLP Pipeline
1.  **Text Preprocessing**: The input is normalized (lowercasing) and tokenized into individual words or segments.
2.  **Segment Analysis**: The engine splits the text by contrast markers (like "but"). It applies a higher weight (1.3x) to segments appearing after a contrast word, as these often contain the reviewer's true conclusion.
3.  **Word-Level Scoring**: 
    -   Words are matched against a curated dictionary of **positive** and **negative** movie-specific tokens.
    -   The engine checks the 1-2 words preceding a token to detect **negations** (flipping the score) or **intensifiers** (multiplying the score).
4.  **Confidence Calculation**:
    -   Confidence is derived from the ratio of positive/negative signals relative to the total word count and intensity.
    -   Mixed reviews (high positive and high negative scores) are automatically classified as **Neutral** with a balanced explanation.

### Frontend Technologies
-   **Tailwind-inspired CSS**: Custom glassmorphism variables.
-   **Chart.js**: Powering the distribution and trend charts.
-   **Canvas-Confetti**: Celebration effects triggered on positive detections.
-   **Lottie-Web**: (Optional) Animation support ready for integration.

---

## 🏁 Conclusion

CineScope AI demonstrates a sophisticated approach to sentiment analysis that prioritizes performance and user experience. By moving the logic to a rule-based engine and using CSS for visuals, the application remains lightweight, private, and extremely fast, while still providing deep insights into audience feedback.

*Developed for the Advanced Agentic Coding - Sentimental Analysis Project.*
