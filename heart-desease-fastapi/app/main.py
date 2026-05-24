from fastapi import FastAPI
from app.schemas import HeartData
from app.model_loader import model
from app.config import *

import pandas as pd

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)

FEATURES = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]

@app.get("/")
def home():
    return {
        "message": "Heart Disease Prediction API is running!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/info")
def info():
    return {
        "model": "Logistic Regression",
        "features": FEATURES,
        "developer": "Your Name"
    }

@app.post("/predict")
def predict(data: HeartData):

    input_data = pd.DataFrame([data.dict()])

    prediction = model.predict(input_data)[0]

    return {
        "heart_disease": bool(prediction)
    }