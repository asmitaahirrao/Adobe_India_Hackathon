# 🧠 Adobe India Hackathon 2025 – Round 1 Submissions

Welcome to our submission for the **Adobe India Hackathon 2025**. This repository includes solutions for both Round 1A and Round 1B challenges.

---

## 📦 Round 1A – Structured Outline Extraction from PDFs

### 🔍 Challenge Name: Connecting the Dots Through Docs (Round 1A)

### 📌 Objective:
To extract structured headings (H1, H2, H3) from scanned Marathi PDF documents using OCR and classify them using a multilingual transformer model.

### 🛠️ Tech Stack:
| Component         | Details                                          |
|-------------------|--------------------------------------------------|
| 🖨️ OCR Engine     | `Tesseract OCR`                                   |
| 📄 PDF Parser     | `PyMuPDF` (`fitz`)                                |
| 🤖 Classifier     | `xlm-roberta-base` via `transformers`             |
| 🧹 Post-Processing| Rule-based corrections for OCR formatting         |
| 🐍 Language       | Python 3.10                                       |
| 🐳 Container      | Docker-based solution                             |

### 🚀 Features:
- ✅ Multilingual heading classification (H1/H2/H3)
- ✅ Rule-based text segmentation and correction
- ✅ Output format in JSON as per Adobe specification
- ✅ OCR + Transformer pipeline for noisy input handling

### 📁 Sample Output:
```json
{
  "title": "झाडे",
  "outline": [
    {
      "level": "H1",
      "text": "झाडे",
      "page": 0,
      "language": "mr"
    },
    {
      "level": "H2",
      "text": "वाचवा",
      "page": 0,
      "language": "mr"
    }
  ]
}
```

---

## 📦 Round 1B – Persona-Based Document Intelligence

### 🔍 Challenge Name: Connecting the Dots Through Docs (Round 1B)

### 📌 Objective:
To extract the most relevant document sections from a group of PDFs based on a given **persona** and **job-to-be-done**, and return the results in structured JSON output.

### 🛠️ Tech Stack:
| Component          | Description                                        |
|--------------------|----------------------------------------------------|
| 📄 PDF Parsing     | `PyMuPDF` (`fitz`)                                 |
| 🤖 Embedding Model | `sentence-transformers` - `all-MiniLM-L6-v2`       |
| 🔍 Similarity      | Cosine similarity via `sentence-transformers.util` |
| 🧠 Ranking Logic   | Semantic block-level scoring                       |
| 🐳 Container       | Docker with `python:3.10-slim`                     |
| 🐍 Language        | Python 3.10                                        |

### 🗃️ Folder Structure:
```
challenge1b/
├── app/
│   ├── main.py
│   ├── analyzer.py
│   ├── pdf_processor.py
│   ├── utils.py
│   └── all-MiniLM-L6-v2/
├── requirements.txt
├── Dockerfile
├── model_download.py
├── input/
├── output/
└── submission_summary.md
```

### 🧪 Run Instructions:
```bash
docker build -t adobe-round1b .

docker run --rm \
  -v "$(pwd)/app/input:/app/input" \
  -v "$(pwd)/app/output:/app/output" \
  --network none adobe-round1b
```

### 📝 Output Structure:
- `metadata`: Persona, task, input references, timestamp
- `extracted_sections`: Top 10 blocks with doc/page reference
- `subsection_analysis`: Full body text for selected blocks

---

## 🙌 Team Notes
Both submissions emphasize clarity, modularity, and real-world applicability. We ensured each solution was scalable and followed the structure expected by Adobe's evaluation guidelines.

---

## 📁 Repository Layout
```
.
├── round1a/               # OCR + Heading Classifier (Round 1A)
│   └── ...                # Code and models
├── challenge1b/           # Persona-based Ranking (Round 1B)
│   └── ...                # Code and outputs
└── README.md              # This file
```

---

## 📧 Contact
For queries, feel free to reach out to the team via GitHub Issues or Discussions.
