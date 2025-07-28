# 🔗 Adobe India Hackathon - Round 1B Submission Summary

## 📌 Challenge Name: Connecting the Dots Through Docs (Round 1B)

---

## 📂 Objective:
To build an intelligent document processing system that extracts the most relevant sections from a set of PDFs based on a given **persona** and **job-to-be-done** (task), and outputs structured insights in a predefined JSON format for multiple groups.

---

## 🛠️ Tools & Technologies Used:

| Component          | Details                                           |
|--------------------|---------------------------------------------------|
| 📄 PDF Parsing     | `PyMuPDF` (`fitz`)                                 |
| 🤖 Embedding Model | `sentence-transformers` - `all-MiniLM-L6-v2`      |
| 🔍 Similarity      | `cosine similarity` from `sentence-transformers.util` |
| 🧠 Ranking         | Relevance-based filtering and similarity scoring  |
| 🐳 Container       | Docker with `python:3.10-slim` base                |
| 🐍 Language        | Python 3.10                                        |

---

## 🧠 Model Used:

### 🔸 SentenceTransformer
- **Name:** `all-MiniLM-L6-v2`
- **Purpose:** Convert textual blocks and task queries into semantic embeddings.
- **Similarity Metric:** Cosine similarity for relevance ranking.

---

## 🗃️ Folder Structure:
```
challenge1b/
├── app/
│   ├── main.py                  # 🔁 Entry point to process all groups
│   ├── analyzer.py              # 🔍 Ranking logic using transformer
│   ├── pdf_processor.py         # 📄 Extracts text blocks from PDFs
│   ├── utils.py                 # 🕓 Timestamp generator
│   └── all-MiniLM-L6-v2/        # 🧠 Local sentence-transformer model
├── requirements.txt             # 📦 Required Python libraries
├── Dockerfile                   # 🐳 Container build definition
├── model_download.py            # 📥 Script to download and save model
├── input/                       # 📂 Folder containing group-wise PDFs and JSONs
├── output/                      # 📂 Generated JSON outputs per group
└── submission_summary.md        # 📄 This file
```

---

## 🧪 How to Run (Windows CMD):

1. ✅ **Build Docker Image**  
   From the root directory:
   ```cmd
   docker build -t adobe-round1b .
   ```

2. 🚀 **Run Docker & Process All Groups**  
   Ensure your group folders and JSONs are in `app/input/`. Then run:
   ```cmd
   docker run --rm -v "%cd%\app\input:/app/input" -v "%cd%\app\output:/app/output" --network none adobe-round1b
   ```

   This will process **all groups** inside `/app/input/`, and generate corresponding:
   ```
   /app/output/<group_name>/challenge1b_output.json
   ```

---

## 📝 Output Format:

Each group generates:
- `challenge1b_output.json` with:
  - `metadata`: includes input docs, persona, task, timestamp
  - `extracted_sections`: top-10 ranked sections with document and page number
  - `subsection_analysis`: full refined text for those sections

---

## ⚙️ Enhancements Implemented:
- ✅ Block-level ranking using semantic similarity
- ✅ JSON validation against expected schema
- ✅ Multi-group batch processing in one command
- ✅ Model loading optimized via local cache
- ✅ Filtered and formatted output aligned with Adobe sample

---

## 🙌 Team Notes:
This project was designed to be scalable, interpretable, and easily testable with multiple PDF groups. Semantic quality of output has been tuned using domain-aware heuristics and pre-trained multilingual models.
