import openai
from flask import Flask, request, render_template
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load the model and scalers
model = pickle.load(open('model.pkl', 'rb'))
scaler = StandardScaler()
minmax_scaler = MinMaxScaler()

# Create the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    N = float(request.form['Nitrogen'])
    P = float(request.form['Phosporus'])
    K = float(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['Ph'])
    rainfall = float(request.form['Rainfall'])
    textgpt=f"tell me what i should grow at{N} where type of soil is {P} and usual temperature is {temp} and weather is {K} and rainfall is {rainfall} "

def chat(textgpt):
    openai.api_key = "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"
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=textgpt,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    hehe=(response["choices"][0]["text"])
    return render_template('index.html', result=hehe)







    # return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
