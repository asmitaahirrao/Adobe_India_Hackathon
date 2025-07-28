import re

def classify_heading_level(text: str) -> str:
    text = text.strip()

    # ❌ Ignore if it's too short or meaningless (less than 6 chars or ends with . ! ?)
    if len(text) < 6 or re.fullmatch(r"[अ-ह|a-zA-Z|0-9\s\.\-]+[.?!]", text):
        return None

    # ❌ Ignore if sentence-like (ends with period and has many words)
    if text.endswith('.') and len(text.split()) > 4:
        return None

    # ✅ Looks like a numbered heading? Accept as H2
    if re.match(r"^\d+\s*[.)।]", text) or re.match(r"^[०१२३४५६७८९]+\s*[.)।]", text):
        return "H2"

    # ✅ Very short title (<= 3 words)? Accept as H1
    if len(text.split()) <= 3 and not text.endswith('.'):
        return "H1"

    # ✅ Short subheading (<= 6 words)? Accept as H3
    if 3 < len(text.split()) <= 6 and not text.endswith('.'):
        return "H3"

    return None
