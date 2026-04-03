from pathlib import Path
import json
import re

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "knowledge" / "raw"
CHUNK_DIR = BASE_DIR / "knowledge" / "chunks"
INDEX_DIR = BASE_DIR / "knowledge" / "index"
CHUNK_DIR.mkdir(parents=True, exist_ok=True)
INDEX_DIR.mkdir(parents=True, exist_ok=True)

DOC_SETTINGS = {
    "01_basiskennis.md": {"document": "01_basiskennis", "default_type": "definition"},
    "02_bouw_onderhoud_checklists.md": {"document": "02_bouw_onderhoud_checklists", "default_type": "procedure"},
    "03_onderwijsformats.md": {"document": "03_onderwijsformats", "default_type": "format"},
    "04_faq_voorbeeldantwoorden.md": {"document": "04_faq_voorbeeldantwoorden", "default_type": "faq"},
}

def infer_type(heading: str, doc_default: str) -> str:
    h = heading.lower()
    if "diagnose" in h:
        return "diagnosis"
    if "taalregels" in h or "escalatieregels" in h or "veilig" in h:
        return "safety_rule"
    if "checklist" in h or "procedure" in h or "kalibratie" in h or "start" in h or "onderhoud" in h:
        return "procedure"
    if "format" in h or "sjabloon" in h or "task card" in h or "logboek" in h or "pve" in h or "user story" in h:
        return "format"
    if "vraag" in h or "voorbeeldantwoord" in h:
        return "faq"
    return doc_default

def extract_headed_sections(markdown: str):
    lines = markdown.splitlines()
    sections = []
    current_heading = "Inleiding"
    current_lines = []
    for line in lines:
        if re.match(r"^##+\s+", line):
            if current_lines:
                sections.append((current_heading, "\n".join(current_lines).strip()))
            current_heading = re.sub(r"^##+\s+", "", line).strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_lines:
        sections.append((current_heading, "\n".join(current_lines).strip()))
    return [(h, c) for h, c in sections if c]

def build_keywords(text: str) -> list[str]:
    tokens = re.findall(r"[A-Za-zÀ-ÿ0-9_-]{3,}", text.lower())
    stop = {"de", "het", "een", "van", "voor", "met", "dat", "als", "bij", "naar", "door", "niet", "ook", "dan"}
    unique = []
    for token in tokens:
        if token in stop:
            continue
        if token not in unique:
            unique.append(token)
    return unique[:12]

def audience_from_heading(heading: str) -> list[str]:
    h = heading.lower()
    if "student" in h:
        return ["student"]
    if "docent" in h:
        return ["docent"]
    return ["student", "docent", "beide"]

def main() -> None:
    all_chunks = []
    grouped = {"definitions": [], "procedures": [], "formats": [], "faq": [], "safety": [], "diagnosis": []}
    for file in sorted(RAW_DIR.glob("*.md")):
        settings = DOC_SETTINGS[file.name]
        text = file.read_text(encoding="utf-8")
        sections = extract_headed_sections(text)
        for idx, (heading, content) in enumerate(sections, start=1):
            chunk_type = infer_type(heading, settings["default_type"])
            chunk = {
                "id": f"{settings['document']}_{idx:03d}",
                "title": heading,
                "document": settings["document"],
                "type": chunk_type,
                "audience": audience_from_heading(heading),
                "topic": build_keywords(heading),
                "safety_level": "escalate" if chunk_type == "safety_rule" else "normal",
                "keywords": build_keywords(content),
                "content": re.sub(r"\n{3,}", "\n\n", content).strip(),
            }
            all_chunks.append(chunk)
            if chunk_type == "definition":
                grouped["definitions"].append(chunk)
            elif chunk_type == "procedure":
                grouped["procedures"].append(chunk)
            elif chunk_type == "format":
                grouped["formats"].append(chunk)
            elif chunk_type == "diagnosis":
                grouped["diagnosis"].append(chunk)
            elif chunk_type == "safety_rule":
                grouped["safety"].append(chunk)
            else:
                grouped["faq"].append(chunk)
    (CHUNK_DIR / "definitions.json").write_text(json.dumps(grouped["definitions"], indent=2, ensure_ascii=False), encoding="utf-8")
    (CHUNK_DIR / "procedures.json").write_text(json.dumps(grouped["procedures"], indent=2, ensure_ascii=False), encoding="utf-8")
    (CHUNK_DIR / "formats.json").write_text(json.dumps(grouped["formats"], indent=2, ensure_ascii=False), encoding="utf-8")
    (CHUNK_DIR / "faq.json").write_text(json.dumps(grouped["faq"] + grouped["diagnosis"] + grouped["safety"], indent=2, ensure_ascii=False), encoding="utf-8")
    (INDEX_DIR / "metadata.json").write_text(json.dumps({"count": len(all_chunks)}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Klaar. {len(all_chunks)} chunks geschreven.")

if __name__ == "__main__":
    main()
