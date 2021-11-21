from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')

def home():

    return render_template('home.html')

@app.route('/predict', methods = ['POST'])

def predict():

    in_features = [float(x) for x in request.form.values()]
    features = [np.array(in_features)]

    prediction = int(model.predict(features))
    
    if prediction == 0:

        opt = 'No Heart Disease'

    else:

        opt = 'Heart Disease'

    return render_template('home.html', output= opt)

if __name__ == "__main__":
    app.run(debug=True)