FROM python:3.10-slim

WORKDIR /app

COPY app.py .
COPY log_reg_model.pkl .
COPY tfidf_vectorizer.pkl .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]