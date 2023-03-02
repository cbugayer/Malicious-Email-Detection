from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import tensorflow as tf
from tensorflow.python import keras
from feature_extraction import feature_extraction
from fastapi.middleware.cors import CORSMiddleware

def load_phishing_detection_model():
    """
    load pretrained phishing detection model from disk
    """
    model = keras.models.load_model("./phishing-detection-model")
    model_inference = model.signatures["serving_default"]
    return model_inference

PhishingDetectionModel = load_phishing_detection_model()

class UrlsIn(BaseModel):
    urls: List[str]

class Prediction(BaseModel):
    url: str
    phishing_probability: int
    prediction: str
class PhishingPrediction(BaseModel):
    predictions: List[Prediction]

app = FastAPI()
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/phishing-prediction", response_model=PhishingPrediction)
def extract_urls(urlsDict: UrlsIn):
    urls = urlsDict.urls
    features = [feature_extraction(url) for url in urls]
    # make inference
    model_preds = PhishingDetectionModel(Input_Layer=tf.cast(tf.convert_to_tensor(features), dtype="float"))
    # get actual preds
    model_preds = model_preds["Output_Layer"]
    predictions = []
    for i,prob in enumerate(model_preds):
        phish_or_not = "Phishing" if prob > 0.8 else "Legitimate"
        pred = {
            "url":urls[i],
            "phishing_probability":int(prob*100),
            "prediction": phish_or_not
        }
        predictions.append(pred)
    return {"predictions" : predictions}
