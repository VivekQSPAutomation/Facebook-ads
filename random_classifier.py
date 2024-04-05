import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("future_data.csv")
df = df.drop(columns=['ip_address'])

# Encode the 'user_agent' column
le = LabelEncoder()
X = le.fit_transform(df['user_agent'])
XX = X.reshape(-1, 1)  # Convert X to a 2D array

y = df['label']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(XX, y, test_size=len(X)-1, random_state=200)

# Create the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=200)

# Fit the classifier to the training data
rf_classifier.fit(X_train, y_train)

# Set the feature names after fitting
rf_classifier.feature_names_ = ['user_agent']

y_pred_train = rf_classifier.predict(X_train)
y_pred_test = rf_classifier.predict(X_test)

# Save the trained model
joblib.dump(rf_classifier, 'trained_model.pkl')

print("Training Accuracy:", accuracy_score(y_train, y_pred_train))
print("Test Accuracy:", accuracy_score(y_test, y_pred_test))
print("\nClassification Report:")
print(classification_report(y_test, y_pred_test, zero_division=1))