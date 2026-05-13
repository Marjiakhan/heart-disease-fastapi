from fastapi import FastAPI
from app.schemas import HeartData
import pandas as pd
import joblib

app = FastAPI()

# Load model
model = joblib.load("model/heart_model.joblib")

@app.get("/")
def root():
    return {"message": "Heart Disease API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/info")
def info():
    return {
        "model": "Logistic Regression",
        "features": [
            "age", "sex", "cp", "trestbps",
            "chol", "fbs", "restecg",
            "thalach", "exang", "oldpeak",
            "slope", "ca", "thal"
        ]
    }

@app.post("/predict")
def predict(data: HeartData):

    input_data = pd.DataFrame([data.dict()])

    prediction = model.predict(input_data)[0]

    return {
        "heart_disease": bool(prediction)
    }