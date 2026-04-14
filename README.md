# 🚀 End-to-End Churn Prediction Pipeline

---

## 📌 Overview

This project is an end-to-end **Customer Churn Prediction System** that uses machine learning to predict whether a customer is likely to leave a service.

It simulates a real-world production pipeline by integrating:

* Model training and evaluation
* Experiment tracking with MLflow
* Model deployment using FastAPI
* Real-time prediction via REST API

---

## ✨ Features

* 📊 Machine Learning model (Random Forest)
* 🧪 Experiment tracking using MLflow
* ⚡ REST API for real-time predictions
* 🧠 Feature engineering & preprocessing
* 🔄 End-to-end ML pipeline

---

## 🧠 Tech Stack

* **Python**
* **Scikit-learn**
* **MLflow**
* **FastAPI**
* **Pandas**
* **Joblib**

---

## 🏗️ Architecture

```
Raw Data
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Model Training (Random Forest)
   ↓
MLflow Tracking
   ↓
Model Saving
   ↓
FastAPI Deployment
   ↓
Prediction API
```

---

## 📂 Project Structure

```
churn-prediction-mlops/
│
├── app/
│   ├── main.py
│   ├── schema.py
│
├── model/
│   ├── train.py
│   ├── predict.py
│   └── model.pkl
│
├── data/
│   └── churn.csv
│
├── mlruns/
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/churn-prediction-mlops.git
cd churn-prediction-mlops
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Train the Model

```bash
python model/train.py
```

---

### 4️⃣ Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

### 5️⃣ Access API Docs

👉 http://127.0.0.1:8000/docs

---

## 📊 API Example

### POST `/predict`

```json
{
  "age": 40,
  "balance": 2000,
  "products": 2,
  "active": 1
}
```

### Response:

```json
{
  "churn_prediction": 1
}
```

---

## 🧪 MLflow Tracking

Run MLflow UI:

```bash
mlflow ui
```

👉 http://127.0.0.1:5000

Track:

* Accuracy
* Model versions
* Experiment runs

---

## 📬 Author

**Joncy Keda - AI Developer**
📧 Add your email
🔗 Add your LinkedIn

---
