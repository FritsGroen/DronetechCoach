from openai import OpenAI
from models import AskRequest, AskResponse, SourceItem
from settings import settings
from safety import check_safety, build_safety_response
from retrieval import load_chunks, classify_question, retrieve_chunks
from prompts import build_system_instructions, build_user_input

client = OpenAI(api_key=settings.openai_api_key)
KNOWLEDGE_CHUNKS = load_chunks(settings.knowledge_dir)

def reload_knowledge() -> int:
    global KNOWLEDGE_CHUNKS
    KNOWLEDGE_CHUNKS = load_chunks(settings.knowledge_dir)
    return len(KNOWLEDGE_CHUNKS)

def build_follow_ups(category: str) -> list[str]:
    mapping = {
        "definition": ["Geef een praktisch voorbeeld", "Wat gaat hierbij vaak mis?", "Welke checklist hoort hierbij?"],
        "procedure": ["Geef de checklist stap voor stap", "Moeten de propellers eraf?", "Wat controleer ik daarna?"],
        "format": ["Maak ook een compact voorbeeld", "Voeg acceptatiecriteria toe", "Maak dit geschikt voor studenten"],
        "diagnosis": ["Geef de bench test checklist", "Wat is de veiligste vervolgstap?", "Wanneer moet ik escaleren?"],
        "docent": ["Maak dit schaalbaar voor een klas", "Welke minimale documentatie hoort erbij?", "Geef ook een korte rubric"],
    }
    return mapping.get(category, ["Geef een korter antwoord", "Geef de checklist", "Geef een voorbeeld"])

def answer_question(payload: AskRequest) -> AskResponse:
    safety = check_safety(payload.message)
    category = classify_question(payload.message, payload.role)
    if safety.escalate:
        return AskResponse(
            answer=build_safety_response(payload.message, payload.role),
            category="safety",
            audience=payload.role,
            safety=safety,
            sources=[],
            suggested_follow_ups=[
                "Beschrijf de schade of foutmelding",
                "Wat is veilig om eerst uit te schakelen?",
                "Welke onderdelen moet de docent controleren?",
            ],
        )
    selected_chunks = retrieve_chunks(payload.message, payload.role, KNOWLEDGE_CHUNKS, category, settings.max_chunks_per_query)
    response = client.responses.create(
        model=settings.openai_model,
        input=[
            {"role": "developer", "content": [{"type": "input_text", "text": build_system_instructions()}]},
            {"role": "user", "content": [{"type": "input_text", "text": build_user_input(payload.message, payload.role, category, selected_chunks)}]},
        ],
    )
    answer_text = response.output_text.strip() if hasattr(response, "output_text") else "Geen antwoord ontvangen."
    sources = [SourceItem(document=chunk.get("document", "onbekend"), title=chunk.get("title", "onbekend"), chunk_id=chunk.get("id")) for chunk in selected_chunks]
    return AskResponse(
        answer=answer_text,
        category=category,
        audience=payload.role,
        safety=safety,
        sources=sources,
        suggested_follow_ups=build_follow_ups(category),
        debug={"matched_chunks": len(selected_chunks)} if settings.app_env != "production" else None,
    )
