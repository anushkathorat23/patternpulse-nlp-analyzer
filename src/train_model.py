import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("training_data.csv")

# Remove empty rows
df = df.dropna()

# Ensure text column is string
df["text"] = df["text"].astype(str)

X = df["text"]
y = df["label"]

# Convert text to numerical features
vectorizer = TfidfVectorizer(stop_words="english")

X_vec = vectorizer.fit_transform(X)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Train classifier
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)

print("\nModel Performance:\n")
print(classification_report(y_test, predictions))

# Save model
joblib.dump(model, "models/classifier.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("\nModel saved successfully in models folder")