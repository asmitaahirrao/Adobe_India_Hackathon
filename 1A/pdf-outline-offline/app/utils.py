import fitz
# PyMuPDF
from classify_headings import classify_heading_level
import re

def extract_outline_from_pdf(pdf_path: str):
    doc = fitz.open(pdf_path)
    filename = pdf_path.split("/")[-1].replace(".pdf", "")

    outline = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if block["type"] != 0:
                continue  # skip images or other non-text blocks

            for line in block["lines"]:
                text = " ".join([span["text"] for span in line["spans"]]).strip()

                # Skip empty or short lines
                if not text or len(text) < 5:
                    continue

                # Predict heading level
                level = classify_heading_level(text)

                # Add only predicted headings (H1/H2/H3)
                if level:
                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num + 1
                    })

    return {
        "title": filename,
        "outline": outline
    }
