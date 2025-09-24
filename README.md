Reply Classification Project – SvaraAI
Overview
This project implements a reply classification pipeline for email replies in outbound sales. The goal is to classify replies into:

positive → Interested in a demo/meeting

neutral → Non-committal or irrelevant

negative → Not interested / rejection

The project consists of:

Part A – ML/NLP Pipeline (Notebook: notebook.ipynb)

Part B – Deployment Task (API) (FastAPI code: app.py)

Part C – Reasoning answers (Markdown: answers.md)

Optional bonus: Docker containerization.

Project Structure
reply_classification_project/
├─ notebook.ipynb          # Part A: ML/NLP Pipeline
├─ app.py                  # Part B: FastAPI API
├─ log_reg_model.pkl       # Trained Logistic Regression model
├─ tfidf_vectorizer.pkl    # Trained TF-IDF vectorizer
├─ requirements.txt        # Python dependencies
├─ Dockerfile              # Optional Docker setup
├─ answers.md              # Reasoning / explanation answers
└─ README.md               # This file


Part A – ML/NLP Pipeline
Notebook: notebook.ipynb

Steps performed:

Dataset Loading and Preprocessing

Loaded CSV dataset of email replies.

Dropped missing values.

Cleaned text: lowercasing, removed URLs, non-alphabetic characters, extra spaces.

Baseline Model – Logistic Regression

TF-IDF vectorization on cleaned text.

Trained Logistic Regression classifier.

Performance:

Accuracy: 0.998

Macro F1-score: 0.998

Balanced class-wise precision and recall.

Transformer Model – DistilBERT (Optional)

Fine-tuned distilbert-base-uncased using Hugging Face.

On this small dataset, it did not outperform Logistic Regression.

Model Evaluation

Accuracy and macro F1 computed.

Logistic Regression chosen as production-ready model due to simplicity, efficiency, and high performance.

Part B – Deployment Task (API)
File: app.py

Features:

FastAPI service with /predict endpoint.

Input: JSON with text, e.g.

{"text": "Looking forward to the demo!"}


Output: JSON with predicted label and confidence, e.g.

{"label": "positive", "confidence": 0.82}


Run Locally (without Docker)
Install dependencies:

pip install -r requirements.txt


Run the API:

uvicorn app:app --host 0.0.0.0 --port 8000


Test endpoint:

import requests

data = {"text": "Looking forward to the demo!"}
response = requests.post("[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)", json=data)
print(response.json())


Run with Docker (Optional Bonus)
Build Docker image:

docker build -t reply-api .


Run container:

docker run -p 8000:8000 reply-api


Test endpoint (same as above).

Note: If you get scikit-learn version warnings, ensure requirements.txt matches the version used to train the models.

Part C – Reasoning / Answers
File: answers.md

Contains explanations for:

Why Logistic Regression was chosen over transformers for production.

Trade-offs in model complexity, performance, and deployment.

Steps followed in preprocessing, modeling, and evaluation.

Requirements
Python packages (requirements.txt):

fastapi
uvicorn
scikit-learn==1.6.1
numpy
pydantic


scikit-learn==1.6.1 ensures compatibility with pickled models.

Usage Notes
Ensure log_reg_model.pkl and tfidf_vectorizer.pkl are in the same folder as app.py.

API can run locally without Docker. Docker is optional for containerized deployment.

Tested successfully in Colab and local environment.

Contact / References
Project implemented as part of SvaraAI ML assignment.

References:

Hugging Face Transformers: https://huggingface.co/docs/transformers

FastAPI: https://fastapi.tiangolo.com/

Scikit-learn: https://scikit-learn.org/
