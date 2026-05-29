# 🎬 CineScope AI — Movie Review Sentiment Analyzer

A beautiful, fully AI-powered sentiment analysis web app for movie reviews.
Built with plain HTML + CSS + JavaScript. No frameworks, no build tools needed.

---

## 🚀 Quick Start

### Step 1 — Get your API Key
1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Sign up / log in
3. Click **"API Keys"** → **"Create Key"**
4. Copy the key (starts with `sk-ant-...`)

### Step 2 — Add your key to the file
Open `index.html` and find this line near the top of the `<script>` section:

```javascript
const API_KEY = 'YOUR_ANTHROPIC_API_KEY';
```

Replace `YOUR_ANTHROPIC_API_KEY` with your actual key:

```javascript
const API_KEY = 'sk-ant-api03-xxxxxxxxxxxxxxxxxx';
```

### Step 3 — Open in browser
Just double-click `index.html` — no server needed!

> 💡 **Tip:** Press `Ctrl + Enter` (or `Cmd + Enter` on Mac) inside the text area to analyze quickly.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🤖 AI Sentiment Analysis | Powered by Claude (claude-sonnet-4) |
| 😊 😞 😐 Sentiment Labels | Positive / Negative / Neutral |
| 📊 Confidence Score | 0–100% with animated meter |
| 🎭 Animated GIFs | Auto-loads matching Giphy GIF |
| 🌈 Word Highlights | Green = positive, Red = negative |
| 💡 AI Explanation | One-sentence reason with key words |
| 📈 Live Charts | Doughnut + Bar (Chart.js) |
| 🕐 History Log | Last 20 reviews with scroll |
| 🌙☀️ Dark/Light Mode | Toggle button, smooth transition |
| ⌨️ Keyboard Shortcut | Ctrl/Cmd + Enter to analyze |
| ✨ Star Background | Animated twinkling stars |
| 📱 Responsive | Mobile + Desktop friendly |

---

## 📁 File Structure

```
cinescope/
└── index.html     ← Single file — everything included!
```

No npm, no build step, no dependencies to install.
Chart.js and Google Fonts load from CDN automatically.

---

## 🎨 Tech Stack

- **HTML5 + CSS3 + Vanilla JS** — no framework needed
- **Claude API** — `claude-sonnet-4-20250514` for sentiment analysis
- **Chart.js 4.4** — pie and bar charts
- **Google Fonts** — Bebas Neue + DM Sans
- **Giphy** — public GIF embeds

---

## 🛡️ Important Notes

- Your API key is in the HTML file — **don't share this file publicly** or commit it to GitHub with the key in it.
- For a production app, move the API call to a backend server so the key stays secret.
- The app uses the **direct browser API access** header (`anthropic-dangerous-direct-browser-access: true`) which is fine for personal/local use.

---

## 🎬 Sample Reviews to Try

**Positive:**
> "The film was absolutely breathtaking — stunning visuals, powerful acting, and a storyline that left me speechless. A true masterpiece!"

**Negative:**
> "Terrible movie. The plot was boring, the acting was wooden, and the ending was a complete disappointment. Don't waste your time."

**Neutral:**
> "The movie had some good moments and some bad ones. The visuals were decent but the story was average. Worth watching if you have nothing else to do."

---

Made with ♥ using Claude AI
