from pathlib import Path
import json
import re

QUESTION_PATTERNS = {
    "definition": ["wat is", "wat betekent", "verschil tussen", "definitie"],
    "format": ["maak een pve", "maak een user story", "user story", "logboek", "task card", "acceptatiecriteria", "format"],
    "diagnosis": ["armt niet", "trilt", "trekt", "motor", "accu warm", "start later", "hoogtehold pompt"],
    "docent": ["hoe beoordeel", "hoe begeleid", "grote groepen", "docent", "didactisch"],
}

def load_chunks(knowledge_dir: str) -> list[dict]:
    chunk_dir = Path(knowledge_dir) / "chunks"
    all_items = []
    for file in chunk_dir.glob("*.json"):
        with open(file, "r", encoding="utf-8") as fh:
            all_items.extend(json.load(fh))
    return all_items

def classify_question(message: str, role: str) -> str:
    m = message.lower().strip()
    if role == "docent":
        if any(p in m for p in QUESTION_PATTERNS["format"]):
            return "format"
        if any(p in m for p in QUESTION_PATTERNS["docent"]):
            return "docent"
    if any(p in m for p in QUESTION_PATTERNS["definition"]):
        return "definition"
    if any(p in m for p in QUESTION_PATTERNS["format"]):
        return "format"
    if any(p in m for p in QUESTION_PATTERNS["diagnosis"]):
        return "diagnosis"
    if any(p in m for p in QUESTION_PATTERNS["docent"]):
        return "docent"
    return "procedure"

def tokenize(text: str) -> list[str]:
    return [t for t in re.split(r"[^a-zA-Z0-9à-ÿ_-]+", text.lower()) if len(t) > 2]

def score_chunk(message: str, chunk: dict, category: str, role: str) -> int:
    score = 0
    tokens = tokenize(message)
    haystack = " ".join([
        chunk.get("title", ""),
        chunk.get("content", ""),
        " ".join(chunk.get("keywords", [])),
        " ".join(chunk.get("topic", [])),
        chunk.get("type", ""),
    ]).lower()
    for token in tokens:
        if token in haystack:
            score += 2
    if chunk.get("type") == category:
        score += 6
    if role in chunk.get("audience", []) or "beide" in chunk.get("audience", []):
        score += 2
    return score

def retrieve_chunks(message: str, role: str, chunks: list[dict], category: str, max_chunks: int = 6) -> list[dict]:
    scored = []
    for chunk in chunks:
        score = score_chunk(message, chunk, category, role)
        if score > 0:
            scored.append((score, chunk))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [chunk for _, chunk in scored[:max_chunks]]
