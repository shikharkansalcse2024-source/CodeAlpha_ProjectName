# Project 2 — FAQ Chatbot for E-commerce

> NLP-powered FAQ chatbot using TF-IDF vectorization and cosine similarity with a Streamlit chat UI

---

## Problem Statement

An e-commerce store receives hundreds of repetitive customer queries daily about shipping, returns, payments, and order tracking. A human agent answering each one manually is time-consuming and expensive. This project builds an intelligent FAQ chatbot that automatically matches user questions to the most relevant answer — even when the wording is different from the original FAQ.

---

## What Was Built

A complete FAQ chatbot system consisting of:
- Text preprocessing pipeline using NLTK
- TF-IDF vectorization for converting text to numbers
- Cosine similarity matching to find the best FAQ answer
- Command-line chatbot interface
- Streamlit-based visual chat UI (bonus feature)

---

## How It Works

```
User types question
        ↓
Clean and preprocess text
(lowercase, remove punctuation, remove stopwords)
        ↓
Convert to TF-IDF vector
(text becomes a list of numbers)
        ↓
Compare against all 10 FAQ vectors
(cosine similarity score for each)
        ↓
Pick highest scoring FAQ
(if score < 0.2 → "didn't understand")
        ↓
Display matched answer
```

---

## What is Cosine Similarity?

```
Every sentence is converted into a "vector" (list of numbers).
Two sentences with SIMILAR words point in SIMILAR directions.

Cosine Similarity measures how similar two vectors are:

Score = 1.0  → Identical meaning
Score = 0.5  → Similar meaning
Score = 0.0  → Completely different
Score < 0.2  → No match found → bot says "didn't understand"
```

---

## FAQ Topics Covered

| # | Question | Topic |
|---|----------|-------|
| 1 | What are your delivery charges? | Shipping |
| 2 | How long does shipping take? | Shipping |
| 3 | What is your return policy? | Returns |
| 4 | How do I track my order? | Orders |
| 5 | Do you offer cash on delivery? | Payment |
| 6 | How can I cancel my order? | Orders |
| 7 | What payment methods do you accept? | Payment |
| 8 | Is international shipping available? | Shipping |
| 9 | How do I contact customer support? | Support |
| 10 | Do you offer discounts for first-time buyers? | Offers |

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Main programming language |
| NLTK 3.9.4 | Text preprocessing (tokenization, stopwords) |
| scikit-learn 1.9.0 | TF-IDF vectorization + cosine similarity |
| Streamlit 1.58.0 | Chat UI in the browser |

---

## NLP Pipeline Explanation

### Step 1 — Text Cleaning
```
Input : "What ARE your Delivery Charges??"
Output: "delivery charges"

Steps:
→ Lowercase        : "what are your delivery charges??"
→ Remove punctuation: "what are your delivery charges"
→ Tokenize         : ["what", "are", "your", "delivery", "charges"]
→ Remove stopwords : ["delivery", "charges"]
→ Join             : "delivery charges"
```

### Step 2 — TF-IDF Vectorization
```
Converts every cleaned FAQ question into a row of numbers.
Words that appear rarely across FAQs get higher importance.
Words that appear everywhere get lower importance.

Vocabulary learned: 23 unique meaningful words
FAQ matrix shape  : (10 FAQs × 23 features)
```

### Step 3 — Cosine Similarity Matching
```
User question vector is compared against all 10 FAQ vectors.
The FAQ with the highest cosine similarity score wins.
If highest score < 0.2 threshold → "Sorry, didn't understand"
```

---

## Test Results

| User Question | Matched FAQ | Score | Correct? |
|---------------|-------------|-------|----------|
| how much do you charge for shipping? | delivery charges FAQ | 0.52 | ✅ Yes |
| how can I return a product | return policy FAQ | ~0.6 | ✅ Yes |
| do you accept credit cards | payment methods FAQ | ~0.7 | ✅ Yes |
| is cod available | cash on delivery FAQ | ~0.5 | ✅ Yes |
| track my package | order tracking FAQ | ~0.6 | ✅ Yes |
| tell me a joke | No match | 0.02 | ✅ Correctly said "didn't understand" |

---

## How to Run

### Install Dependencies
```
pip install nltk scikit-learn streamlit
```

### Download NLTK Data (one time only)
```
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```

### Run Command-Line Chatbot
```
python src/chatbot.py
```

### Run Streamlit Chat UI
```
python -m streamlit run app.py
```
Then open `http://localhost:8501` in your browser.

---

## Folder Structure

```
FAQ-Chatbot/
├── data/
│   └── faqs.json           ← 10 FAQ questions and answers
├── src/
│   ├── preprocess.py        ← text cleaning functions (NLTK)
│   ├── matcher.py           ← TF-IDF vectorizer + cosine similarity
│   └── chatbot.py           ← command-line chatbot loop
├── app.py                   ← Streamlit chat UI
├── requirements.txt         ← list of required libraries
└── README.md
```

---

## Key Learnings

- NLP preprocessing (cleaning) is the most critical step — dirty text leads to wrong matches
- TF-IDF automatically learns which words are important without any training data
- Cosine similarity is an effective, fast technique for FAQ matching without needing ML model training
- A similarity threshold prevents the bot from giving confidently wrong answers
- Streamlit makes it incredibly easy to build a professional-looking UI with pure Python

---

## Screenshots

*(Add your chatbot UI screenshots here)*

---

*Completed: June 2026 | AI/ML Internship Program*
