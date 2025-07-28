import fitz  # PyMuPDF

def extract_text_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    blocks = []
    for page_number, page in enumerate(doc):
        for block in page.get_text("dict")["blocks"]:
            if "lines" in block:
                text = ""
                for line in block["lines"]:
                    for span in line["spans"]:
                        text += span["text"] + " "
                blocks.append({
                    "page": page_number,
                    "text": text.strip()
                })
    return blocks
