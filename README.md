<div align="center">

# 🏗️ Construction Plan Classification & Sensitive Data Redaction

Automated system for **classifying construction drawing PDFs** and **redacting sensitive information**.

<br>

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![NLP](https://img.shields.io/badge/NLP-Text%20Processing-green)
![Machine Learning](https://img.shields.io/badge/ML-Document%20Classification-orange)
![Regex](https://img.shields.io/badge/Regex-Pattern%20Matching-yellow)

</div>

---

## 🌟 Overview

Construction drawings contain critical design information and often include sensitive data such as client names, project identifiers, and contact information.

This project provides an automated solution to **classify construction drawing PDFs and redact sensitive information before sharing them**.

The system analyzes textual content, structural patterns, and keywords to categorize drawings into their respective engineering disciplines while ensuring that confidential data is removed.

---

## 🎯 Problem Statement

Construction drawings belong to different engineering disciplines and frequently contain confidential information.

The goal of this project is to:

### 1️⃣ Classification

Automatically classify construction drawing PDFs into six categories:

* Architectural
* Structural
* Mechanical
* Plumbing
* Electrical
* Fire Protection

### 2️⃣ Redaction

Detect and redact sensitive information from PDFs while keeping the drawings usable.

---

## 💡 Solution

The system builds an **end-to-end processing pipeline** that performs both classification and redaction.

✔ Extract textual information from PDF drawings
✔ Identify discipline-specific keywords and patterns
✔ Classify drawings into engineering categories
✔ Detect confidential information using **NLP and Regex**
✔ Automatically redact sensitive information

---

## ⚙️ System Workflow

1️⃣ Input construction drawing PDFs
2️⃣ Extract text and layout information
3️⃣ Feature engineering using keywords and title blocks
4️⃣ Document classification
5️⃣ Sensitive information detection
6️⃣ Redaction process
7️⃣ Structured output generation

---

## 🧠 System Architecture

```
Input Construction PDFs
        │
        ▼
Text Extraction
        │
        ▼
Feature Engineering
(Keywords + Layout + Title Blocks)
        │
        ▼
Classification Model
        │
        ▼
Sensitive Information Detection
        │
        ▼
Redaction Engine
        │
        ▼
Output
(Classification CSV + Redacted PDFs)
```

---

## 🛠️ Tech Stack

| Technology       | Purpose                       |
| ---------------- | ----------------------------- |
| Python           | Core programming language     |
| NLP              | Text analysis                 |
| Regex            | Pattern detection             |
| Machine Learning | Document classification       |
| PDF Processing   | Text extraction and redaction |

---

## 📂 Project Structure

```
project
│
├── app.py
├── classifier.py
├── redaction.py
├── requirements.txt
├── README.md
│
├── input_pdfs
│
└── output
    ├── classification_results.csv
    └── redacted_pdfs
```

---

## 🚀 Installation

Clone the repository

git clone https://github.com/yourusername/projectname.git

Navigate to project directory

cd projectname

Install dependencies

pip install -r requirements.txt

Run the system

python app.py

---

## 📊 Output

### Classification Results

PDF Name | Predicted Class | Confidence Score

### Redacted PDFs

Sensitive information is automatically removed while preserving drawing usability.

---

## 🔒 Sensitive Information Redacted

• Person names
• Phone numbers
• Email addresses
• Mailing addresses
• Project numbers
• Internal identifiers
• Signatures

---

## 🚀 Future Improvements

• Improve classification accuracy using deep learning
• Layout-based document understanding
• Web interface for uploading PDFs
• Cloud deployment

---

## ⭐ Contribution

Contributions and improvements are welcome.
