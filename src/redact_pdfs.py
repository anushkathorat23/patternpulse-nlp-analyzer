import os
import fitz
from extract_text import extract_text
from detect_sensitive_info import detect_sensitive_info

INPUT_FOLDER = "dataset/Data to be Classified and Redacted"
OUTPUT_FOLDER = "outputs/redacted_pdfs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(INPUT_FOLDER, file)

        print("Processing:", file)

        doc = fitz.open(pdf_path)

        # Extract text
        text = extract_text(pdf_path)

        # Detect sensitive items
        sensitive_items = detect_sensitive_info(text)

        print("Sensitive items found:", sensitive_items)

        for page in doc:

            for item in sensitive_items:

                areas = page.search_for(item)
                if areas:
                    for area in areas:
                        page.add_redact_annot(area, fill=(0,0,0))

            page.apply_redactions()

        output_path = os.path.join(OUTPUT_FOLDER, file)

        doc.save(output_path)

        doc.close()

print("\nRedaction completed.")