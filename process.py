import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
import numpy as np

def load_models():
    models = {}
    model_names = ['LogisticModel', 'LinearModel', 'SVMmodel']
    for model_name in model_names:
        with open(f'models/{model_name}.pkl', 'rb') as f:
            models[model_name] = pickle.load(f)
    return models

models = load_models()

def extract_features(url):
    return np.random.rand(1, 10)

def predict(url):
    features = extract_features(url)
    predictions = {name: model.predict(features)[0] for name, model in models.items()}

    final_prediction = max(predictions, key=predictions.get)
    
    if final_prediction == "LogisticModel":
        result = "The URL is safe"
        color = "green"
        image = "default.jpg"
    elif final_prediction == "LinearModel":
        result = "The URL is suspicious"
        color = "orange"
        image = "trap.jpg"
    elif final_prediction == "SVMmodel":
        result = "The URL is dangerous"
        color = "red"
        image = "images.jpg"
    else:
        result = "Unable to evaluate"
        color = "black"
        image = "default.jpg"

    return result, color, image
