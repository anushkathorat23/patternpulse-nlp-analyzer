import os
import joblib
import pandas as pd
import re

from extract_text import extract_text

# Keyword dictionary
discipline_keywords = {

    "Architectural": [
        "floor plan", "elevation", "section", "door", "window"
    ],

    "Structural": [
        "beam", "column", "rebar", "foundation", "reinforcement"
    ],

    "Mechanical": [
        "hvac", "duct", "ventilation", "air handling unit"
    ],

    "Plumbing": [
        "pipe", "drain", "fixture", "water supply"
    ],

    "Electrical": [
        "lighting", "switch", "panel", "circuit"
    ],

    "Fire Protection": [
        "sprinkler", "fire alarm", "hydrant", "fire pump"
    ]
}


# Keyword detection
def detect_keyword_class(text):

    text = text.lower()

    for discipline, words in discipline_keywords.items():
        for word in words:
            if word in text:
                return discipline

    return None


# Sheet pattern detection
def detect_sheet_type(text, filename):

    combined = (text + " " + filename).upper()

    if re.search(r"\bA\d+", combined):
        return "Architectural"

    if re.search(r"\bS\d+", combined):
        return "Structural"

    if re.search(r"\bM\d+", combined):
        return "Mechanical"

    if re.search(r"\bP\d+", combined):
        return "Plumbing"

    if re.search(r"\bE\d+", combined):
        return "Electrical"

    if re.search(r"\bFP\d+", combined):
        return "Fire Protection"

    return None


# Load trained model
model = joblib.load("models/classifier.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

TEST_FOLDER = "dataset/Data to be Classified and Redacted"

results = []

print("Starting prediction on test PDFs...\n")

for file in os.listdir(TEST_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(TEST_FOLDER, file)

        print("Processing:", file)

        try:

            text = extract_text(pdf_path)

            text = text.lower()
            text = text.replace("\n", " ")
            text = text.replace("\r", " ")

            # 1️⃣ Sheet detection
            sheet_prediction = detect_sheet_type(text, file)

            # 2️⃣ Keyword detection
            keyword_prediction = detect_keyword_class(text)

            if sheet_prediction:

                predicted_class = sheet_prediction
                confidence = 0.95

            elif keyword_prediction:

                predicted_class = keyword_prediction
                confidence = 0.90

            else:

                X = vectorizer.transform([text])

                predicted_class = model.predict(X)[0]

                probabilities = model.predict_proba(X)[0]

                confidence = max(probabilities)

            results.append({
                "filename": file,
                "predicted_class": predicted_class,
                "confidence": round(confidence, 3)
            })

        except Exception as e:

            print("Error processing:", file)
            print(e)


df = pd.DataFrame(results)

output_path = "outputs/predictions.csv"

df.to_csv(output_path, index=False)

print("\nPrediction completed!")
print("Results saved to:", output_path)