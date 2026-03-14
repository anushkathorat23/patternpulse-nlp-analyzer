import os
import pandas as pd
from extract_text import extract_text

# path to dataset folder
DATASET_PATH = "dataset"

classes = [
    "Architectural",
    "Structural",
    "Mechanical",
    "Plumbing",
    "Electrical",
    "Fire Protection"
]

data = []

for label in classes:

    folder = os.path.join(DATASET_PATH, label)

    print("Reading folder:", folder)

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(folder, file)

            try:
                 text = extract_text(pdf_path)
                 text = text.replace("\n", " ")
                 text = text.replace("\r", " ")
                 
                 data.append({
                     "text": text,
                     "label": label
})
 
            except:
                print("Error reading:", pdf_path)

df = pd.DataFrame(data)

print("Total documents:", len(df))

df.to_csv("training_data.csv", index=False)

print("Training dataset saved as training_data.csv")