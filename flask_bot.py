import joblib
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier

# Load the trained model
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=200)
rf_classifier = joblib.load('trained_model.pkl')  # Assuming you have saved the trained model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    user_agent = request.headers.get('User-Agent')
    new_request_data = [user_agent]
    new_request_df = pd.DataFrame({'user_agent': new_request_data})

    # Perform any necessary data preprocessing on the user_agent string
    # This could include cleaning, feature extraction, or other transformations
    # based on your specific use case and how the model was trained

    new_request_prediction = rf_classifier.predict(new_request_df)
    print(new_request_prediction)
    if new_request_prediction[0] == 1:
        prediction = "The new incoming request is predicted to be from a bot."
    else:
        prediction = "The new incoming request is predicted to be from a real user."

    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(debug=True)
