
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

#create an instance of the FastAPI class
app = FastAPI()
pickle_in = open("rfc_classifier_model.pkl", "rb")
classifier = pickle.load(pickle_in)

#define a route for the root URL
@app.get('/')
def index():
    return {"message": "Hello, World!"}

## Route with single parameter
@app.get('/{name}')
def get_name(name: str):
    return {"Welcome to fast api channel": f"Hello, {name}!"}

#Expose the prediction functionality, make a prediction from the passed JSON
#data and return the predicted Bank Note with the confidence(probability) of the prediction
@app.post('/predict')
def predict_banknote(data: BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if(prediction[0]>0.5):
        prediction = "Fake note"
    else:
        prediction = "It's a Bank note"
    return{
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
# uvicorn app:app --reload