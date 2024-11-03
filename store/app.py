# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('wedding_budget_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    guest_count = int(request.form['guest_count'])
    package_id = int(request.form['package_id'])

    # Get the package cost based on the selected package_id
    package_df = pd.read_csv('packages.csv')
    package_cost = package_df.loc[package_df['Package_ID'] == package_id, 'Package_Cost'].values[0]

    # Prepare the input for prediction
    input_features = np.array([[guest_count, package_cost]])

    # Make prediction
    predicted_budget = model.predict(input_features)[0]

    return jsonify({'predicted_budget': round(predicted_budget, 2)})

if __name__ == '__main__':
    app.run(debug=True)
