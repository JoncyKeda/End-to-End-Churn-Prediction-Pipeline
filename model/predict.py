import joblib
import pandas as pd

model = joblib.load("model/model.pkl")

def predict(data: dict):
    df = pd.DataFrame([data])

    # Match training format
    df = pd.get_dummies(df)

    prediction = model.predict(df)[0]

    return int(prediction)
