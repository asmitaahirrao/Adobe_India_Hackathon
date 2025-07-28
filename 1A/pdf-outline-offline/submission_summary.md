# 🧠 Adobe India Hackathon - Round 1 Submission Summary

## 📌 Challenge Name: Connecting the Dots Through Docs (Round 1A)

## 📂 Objective

To extract structured outlines (H1, H2, H3 headings) from Marathi PDF files using OCR-processed text. The process involves cleaning broken OCR text using rule-based logic, classifying headings using a multilingual transformer model, and generating JSON output with structured hierarchy.

## 🛠️ Tools & Technologies Used

- 🔤 OCR Cleanup: Rule-based Marathi corrections (`ocr_corrections.py`)
- 🤖 ML Model: `bert-base-multilingual-cased` from HuggingFace
- 📚 Libraries: `transformers`, `torch`, `PyMuPDF`, `re`
- 🐍 Programming Language: Python 3.9

## 🧠 Model Details

- Model Used: `bert-base-multilingual-cased`
- Platform: HuggingFace Transformers
- Task: Classify text blocks into:
  - `H1` – Main heading
  - `H2` – Subheading
  - `H3` – Sub-subheading
  - `None` – Non-heading text

⚠️ Note: The actual model weight file (`model.safetensors`) has been excluded from this submission due to file size restrictions. Please use the provided `download_model.py` script to fetch the model automatically.

## 📁 Folder Structure

pdf-outline-offline/  
├── app/  
│   ├── input/                   → Sample input PDFs  
│   ├── output/                  → Output JSON folder  
│   ├── model/                   → Config, tokenizer, vocab (weights excluded)  
│   ├── main.py                  → Main execution script  
│   ├── utils.py                 → Parsing, cleaning logic  
│   ├── classify_headings.py     → Transformer inference  
│   └── ocr_corrections.py       → Rule-based OCR fixes  
├── download_model.py            → Script to download model weights  
├── requirements.txt             → Python dependency file  
├── README.md                    → Setup and usage instructions  
├── Dockerfile                   → For containerized build (optional)  
├── submission_summary.md        → This file

## 🧪 How to Run the Project

1. Create a virtual environment:  
   `python3 -m venv venv`  
   `source venv/bin/activate`

2. Install dependencies:  
   `pip install -r requirements.txt`

3. Download the model:  
   `python download_model.py`

4. Run the application:  
   `python app/main.py`
