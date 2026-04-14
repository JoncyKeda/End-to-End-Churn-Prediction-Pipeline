import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import joblib

# Load dataset
df = pd.read_csv("data/churn.csv")

# Preprocessing
df = df.dropna()

X = df.drop("churn", axis=1)
y = df["churn"]

# Convert categorical variables
X = pd.get_dummies(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Start MLflow
mlflow.start_run()

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
accuracy = accuracy_score(y_test, preds)

# Log metrics
mlflow.log_metric("accuracy", accuracy)
mlflow.sklearn.log_model(model, "model")

# Save model
joblib.dump(model, "model/model.pkl")

print(f"Model trained with accuracy: {accuracy}")

mlflow.end_run()
