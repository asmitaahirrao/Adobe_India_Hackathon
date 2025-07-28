import os
import json
from pdf_processor import extract_text_blocks
from analyzer import rank_sections
from utils import get_timestamp

input_root = "/app/input"
output_root = "/app/output"

# Loop through all group folders
for group_name in os.listdir(input_root):
    group_path = os.path.join(input_root, group_name)
    if not os.path.isdir(group_path):
        continue

    print(f"📁 Processing group: {group_name}")

    # Read JSON input
    json_path = os.path.join(group_path, "challenge1b_input.json")
    if not os.path.exists(json_path):
        print(f"❌ Skipping {group_name}: challenge1b_input.json not found.")
        continue

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    persona = data["persona"]["role"]
    job = data["job_to_be_done"]["task"]
    documents = data["documents"]

    print(f"👤 Persona: {persona}")
    print(f"🧩 Job: {job}")

    extracted = []
    for doc in documents:
        filename = doc["filename"]
        title = doc["title"]
        pdf_path = os.path.join(group_path, filename)

        if not os.path.exists(pdf_path):
            print(f"⚠️ File not found: {filename}, skipping.")
            continue

        print(f"📄 Processing: {filename}")
        blocks = extract_text_blocks(pdf_path)
        ranked = rank_sections(blocks, persona, job)
        for sec in ranked:
            sec["document"] = filename
        extracted.extend(ranked)

    output_json = {
        "metadata": {
            "documents": [doc["filename"] for doc in documents],
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": get_timestamp()
        },
        "extracted_sections": extracted,
        "subsection_analysis": [
            {
                "document": sec["document"],
                "page_number": sec["page_number"],
                "refined_text": sec["section_title"]
            } for sec in extracted
        ]
    }

    output_dir = os.path.join(output_root, group_name)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "challenge1b_output.json")
    with open(output_path, "w", encoding="utf-8") as out_f:
        json.dump(output_json, out_f, indent=2)

    print(f"✅ Output saved: {output_path}\n")
