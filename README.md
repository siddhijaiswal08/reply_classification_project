# Reply Classification Project – SvaraAI

## Overview

This project implements a **reply classification pipeline** for email replies in outbound sales. The goal is to classify replies into:

- `positive` → Interested in a demo/meeting  
- `neutral` → Non-committal or irrelevant  
- `negative` → Not interested / rejection  

The project consists of:

1. **Part A – ML/NLP Pipeline** (Notebook: `notebook.ipynb`)  
2. **Part B – Deployment Task (API)** (FastAPI code: `app.py`)  
3. **Part C – Reasoning answers** (Markdown: `answers.md`)  

Optional bonus: **Docker containerization**.

---

## Project Structure
reply_classification_project/
notebook.ipynb          # Part A: ML/NLP Pipeline
app.py                  # Part B: FastAPI API
log_reg_model.pkl       # Trained Logistic Regression model
tfidf_vectorizer.pkl    # Trained TF-IDF vectorizer
requirements.txt        # Python dependencies
Dockerfile              # Optional Docker setup
answers.md              # Reasoning / explanation answers
README.md               # This file


---

## Part A – ML/NLP Pipeline

**Notebook:** `notebook.ipynb`  

**Steps performed:**

1. **Dataset Loading and Preprocessing**
   - Loaded CSV dataset of email replies.  
   - Dropped missing values.  
   - Cleaned text: lowercasing, removed URLs, non-alphabetic characters, extra spaces.  

2. **Baseline Model – Logistic Regression**
   - TF-IDF vectorization on cleaned text.  
   - Trained Logistic Regression classifier.  
   - Performance:  
     - Accuracy: 0.998  
     - Macro F1-score: 0.998  
   - Balanced class-wise precision and recall.

3. **Transformer Model – DistilBERT (Optional)**
   - Fine-tuned `distilbert-base-uncased` using Hugging Face.  
   - On this small dataset, it did **not outperform Logistic Regression**.  

4. **Model Evaluation**
   - Accuracy and macro F1 computed.  
   - Logistic Regression chosen as **production-ready model** due to simplicity, efficiency, and high performance.

---

## Part B – Deployment Task (API)

**File:** `app.py`  

**Features:**

- FastAPI service with `/predict` endpoint.
- Input: JSON with text, e.g.  
  ```json
  {"text": "Looking forward to the demo!"}
  ## Output

JSON with predicted label and confidence:

```json
{"label": "positive", "confidence": 0.82}



