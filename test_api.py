import requests

# Define the URL and input data
url = "http://127.0.0.1:5000/predict"
input_data = {
    "features": [0.04, 0.05, -0.01, 0.1, 0.2, 0.3, -0.03, 0.02, -0.02, 0.03]
}

# Send POST request
response = requests.post(url, json=input_data)

# Print response
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Error:", response.json())
