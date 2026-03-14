import re
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Regex patterns
phone_pattern = r"\+?\d[\d\s\-]{8,}\d"
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
project_pattern = r"Project\s*(ID|No|Number)?\s*[:\-]?\s*\w+"
job_pattern = r"Job\s*(ID|No|Number)?\s*[:\-]?\s*\w+"
filepath_pattern = r"[A-Za-z]:\\[^\s]+"

def detect_sensitive_info(text):

    sensitive_items = []

    # Clean text
    text = text.replace("\n", " ").replace("\r", " ")

    # Detect phone numbers
    phones = re.findall(phone_pattern, text)
    sensitive_items.extend(phones)

    # Detect emails
    emails = re.findall(email_pattern, text)
    sensitive_items.extend(emails)

    # Detect project identifiers
    projects = re.findall(project_pattern, text)
    sensitive_items.extend(projects)

    # Detect job numbers
    jobs = re.findall(job_pattern, text)
    sensitive_items.extend(jobs)

    # Detect file paths
    paths = re.findall(filepath_pattern, text)
    sensitive_items.extend(paths)

    # Detect names and organizations using spaCy
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG"]:
            sensitive_items.append(ent.text)

    # Remove duplicates
    sensitive_items = list(set(sensitive_items))

    return sensitive_items


# Test block
if __name__ == "__main__":

    sample_text = """
    Engineer: John Smith
    Phone: +91 9876543210
    Email: johnsmith@email.com
    Client: ABC Construction
    Project ID: PRJ-2245
    """

    result = detect_sensitive_info(sample_text)

    print("Sensitive items detected:\n")
    print(result)