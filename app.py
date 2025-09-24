"""
app.py – Reply Classification API (FastAPI)
Author: Your Name
Description: FastAPI service wrapping the Logistic Regression + TF-IDF model 
for classifying email replies into positive, neutral, or negative.
"""

import pickle, re, numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# -------------------------------
# Load model and vectorizer
# -------------------------------
with open("log_reg_model.pkl", "rb") as f:
    log_reg = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

# -------------------------------
# FastAPI setup
# -------------------------------
app = FastAPI(title="Reply Classification API", version="1.0")

class InputText(BaseModel):
    text: str

# Label mapping
inv_label_map = {0: "negative", 1: "neutral", 2: "positive"}

# -------------------------------
# /predict endpoint
# -------------------------------
@app.post("/predict")
def predict(input: InputText):
    """
    Input: JSON {"text": "some text"}
    Output: JSON {"label": "positive", "confidence": 0.87}
    """
    # Clean the input text (same preprocessing as training)
    text_clean = input.text.lower()
    text_clean = re.sub(r"http\S+", " ", text_clean)
    text_clean = re.sub(r"[^a-z\s]", " ", text_clean)
    text_clean = re.sub(r"\s+", " ", text_clean).strip()
    
    # Transform and predict
    vec = tfidf.transform([text_clean])
    pred_label = log_reg.predict(vec)[0]
    pred_prob = np.max(log_reg.predict_proba(vec))
    
    return {
        "label": inv_label_map[pred_label],
        "confidence": float(round(pred_prob, 2))
    }

# -------------------------------
# Run server (for testing only)
# -------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
