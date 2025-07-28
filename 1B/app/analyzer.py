from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('./app/all-MiniLM-L6-v2')

def rank_sections(blocks, persona, job):
    query = f"{persona} needs to {job}"
    query_embedding = model.encode(query, convert_to_tensor=True)

    scored = []
    for block in blocks:
        text = block["text"]
        score = util.cos_sim(model.encode(text, convert_to_tensor=True), query_embedding).item()
        scored.append({
            "document": "",  # We'll fill this in main.py
            "page_number": block["page"],
            "section_title": text[:80],
            "importance_rank": score
        })

    scored.sort(key=lambda x: x["importance_rank"], reverse=True)
    return scored[:10]  # top 10 sections
