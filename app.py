
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('linear_regression_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # Serves the HTML page

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = request.form.get('features', '')  # Get input from the form
        features = [float(x) for x in features.split(',')]  # Parse input into a list of floats
        prediction = model.predict([features]).tolist()
        return render_template('index.html', prediction=prediction[0])
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
