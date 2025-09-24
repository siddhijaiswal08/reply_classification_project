
```markdown
# Reply Classification Project

This repository contains a **reply classification pipeline** to categorize email replies into `positive`, `negative`, or `neutral`. It includes:

- **Part A** – Machine Learning/NLP Pipeline
- **Part B** – Deployment API (FastAPI)
- **Part C** – Reasoning and answers (answers.md)

---

## **Project Structure**

```

.
├─ notebook.ipynb            # Part A & Part C code
├─ app.py                    # FastAPI code for Part B
├─ log\_reg\_model.pkl          # Trained Logistic Regression model
├─ tfidf\_vectorizer.pkl       # TF-IDF vectorizer used for model
├─ requirements.txt           # Python dependencies
├─ Dockerfile                 # Optional Docker setup for Part B
├─ answers.md                 # Reasoning answers for Part A/B

````

---

## **Setup Instructions**

### **1️⃣ Clone Repository**

```bash
git clone <repository_url>
cd <repository_folder>
````

---

### **2️⃣ Setup Python Environment**

It is recommended to use a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### **3️⃣ Run Part A Notebook (Optional)**

* Open `notebook.ipynb` in Jupyter Notebook or Colab.
* Execute all cells to reproduce **ML pipeline, preprocessing, and evaluation results**.

---

### **4️⃣ Run FastAPI API (Part B)**

#### **Option 1 – Locally without Docker**

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

* The API will run at `http://127.0.0.1:8000`
* Test endpoint:

```bash
POST http://127.0.0.1:8000/predict
Content-Type: application/json

{
  "text": "Looking forward to the demo!"
}
```

* Expected response:

```json
{
  "label": "positive",
  "confidence": 0.82
}
```

---

#### **Option 2 – Using Docker (Optional Bonus)**

1. Build Docker image:

```bash
docker build -t reply-api .
```

2. Run Docker container:

```bash
docker run -p 8000:8000 reply-api
```

3. API will run at `http://127.0.0.1:8000` (test same as above).

---

### **5️⃣ Test the API (Python Example)**

```python
import requests

test_data = {"text": "Looking forward to the demo!"}
response = requests.post("http://127.0.0.1:8000/predict", json=test_data)
print(response.json())
```

* Example output:

```json
{"label": "positive", "confidence": 0.82}
```

---

### **6️⃣ Notes**

* Make sure `log_reg_model.pkl` and `tfidf_vectorizer.pkl` are in the same folder as `app.py`.
* `Dockerfile` and `requirements.txt` are provided for containerized deployment.
* The Logistic Regression + TF-IDF model is **production-ready** for this small dataset.
* For larger datasets or more complex language patterns, transformer models can be explored.

---

### **7️⃣ References**

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Scikit-learn Documentation](https://scikit-learn.org/stable/)
* [Uvicorn Documentation](https://www.uvicorn.org/)
* [Docker Documentation](https://docs.docker.com/)

```

---

This `README.md` is **ready-to-upload to GitHub**, formatted properly in Markdown, with all instructions to run both **Part A** and **Part B**, plus Docker.  

If you want, I can also **prepare a `requirements.txt`** that locks scikit-learn to **1.6.1** to avoid any pickle warnings. Do you want me to do that too?
```
