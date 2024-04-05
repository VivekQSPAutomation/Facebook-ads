import numpy as np
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import joblib
import os

app = Flask(__name__)
data_csv_path = 'future_data.csv'
model_path = 'bot_detection_model_rf.joblib'
scaler_path = 'scaler_rf.joblib'
data = pd.read_csv("future_data.csv")
def train_model():
    global data, model, scaler
    try:
        user_agent_dummies = pd.get_dummies(data['user_agent'])
        ip_address_dummies = pd.get_dummies(data['ip_address'])
        X = pd.concat([user_agent_dummies, ip_address_dummies], axis=1)
        y = data['label']

        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, stratify=y, random_state=42)

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True, zero_division=1)

        with open(model_path, 'wb') as model_file:
            joblib.dump(model, model_file)
        with open(scaler_path, 'wb') as scaler_file:
            joblib.dump(scaler, scaler_file)
        return {'model': model, 'scaler': scaler, 'report': report}
    except Exception as e:
        return {'error': str(e)}


@app.route('/real_time_data', methods=['POST'])
def real_time_data():
    global data
    try:
        user_agent = request.headers.get('User-Agent')
        ip_address = request.remote_addr

        if user_agent.strip() and user_agent is not None:
            user_agent_lower = user_agent.lower()
            label = 1 if any(
                keyword in user_agent_lower for keyword in ['bot', 'postman', 'crawl', 'spider', 'slurp']) else 0

            new_data = pd.DataFrame([[user_agent, ip_address, label]],
                                    columns=['user_agent', 'ip_address', 'label'])
            with open(data_csv_path, 'a') as file:
                new_data.to_csv(file, header=False, index=False)
            data = pd.concat([data, new_data], ignore_index=True)
            data['label'] = data['label'].astype(int)
            # data.to_csv(data_csv_path, mode='a', header=False, index=False)
            result = train_model()
            if 'error' in result:
                return jsonify(result)
            else:
                report = result['report']
                return jsonify(report)
        else:
            return jsonify({'error': "User agent cannot be empty"})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    if os.path.isfile(model_path) and os.path.isfile(scaler_path):
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
    else:
        model = None
        scaler = None
    app.run(debug=True)