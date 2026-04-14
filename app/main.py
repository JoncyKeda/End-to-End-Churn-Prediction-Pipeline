from fastapi import FastAPI
from app.schema import CustomerData
from model.predict import predict

app = FastAPI(title="Customer Churn Prediction API")

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def get_prediction(data: CustomerData):
    result = predict(data.dict())
    return {"churn_prediction": result}
