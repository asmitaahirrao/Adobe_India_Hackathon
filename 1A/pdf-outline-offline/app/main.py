import os
import json
import fitz
from utils import extract_outline_from_pdf

def main():
    input_dir = "app/input"
    output_dir = "app/output"

    os.makedirs(output_dir, exist_ok=True)

    print("📥 Reading input directory:", input_dir)
    print("📤 Writing to output directory:", output_dir)

    for file in os.listdir(input_dir):
        print("➡️ Found file:", file)

        if file.endswith(".pdf"):
            path = os.path.join(input_dir, file)
            print("📄 Processing:", path)

            try:
                result = extract_outline_from_pdf(path)

                out_file = file.replace(".pdf", ".json")
                output_path = os.path.join(output_dir, out_file)

                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)

                print("✅ Saved output to:", output_path)

            except Exception as e:
                print("❌ Error while processing:", file)
                print("🔍 Exception:", str(e))

if __name__ == "__main__":
    main()
