from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np

app = FastAPI()

class TextRequest(BaseModel):
    text: str

# Load the saved model
model = tf.keras.models.load_model("metridash_model.h5")
tokenizer = Tokenizer()

@app.post("/predict/")
def predict(text_request: TextRequest):
    text = text_request.text
    token_text = tokenizer.texts_to_sequences([text])[0]
    padded_token_text = pad_sequences([token_text], maxlen=41, padding='pre')
    pos = np.argmax(model.predict(padded_token_text))
    response = {"prediction": pos}
    return response