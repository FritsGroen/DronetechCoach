from models import SafetyResult

ESCALATE_KEYWORDS = [
    "rook", "hitte", "brand", "elektrische schade", "kortsluiting",
    "crash", "harde landing", "ernstige trilling", "ernstige trillingen",
    "trilling", "trillingen", "accu warm", "accu heet", "verbrand",
    "letsel", "gevaar", "aansprakelijkheid"
]

def check_safety(message: str) -> SafetyResult:
    lowered = message.lower()
    matched = [kw for kw in ESCALATE_KEYWORDS if kw in lowered]
    if matched:
        return SafetyResult(level="escalate", escalate=True, matched_keywords=matched)
    return SafetyResult(level="normal", escalate=False, matched_keywords=[])

def build_safety_response(message: str, role: str) -> str:
    if role == "docent":
        return (
            "Dit is een veiligheidskritische situatie. Laat niet verder vliegen of testen. "
            "Maak het systeem spanningsloos, verwijder propellers als dat veilig kan en laat een docent of werkplaatsbegeleider de drone beoordelen. "
            "Noteer daarna kort wat er gebeurde: rook, hitte, schade, foutmelding of trilling."
        )
    return (
        "Stop hier eerst mee en vlieg niet verder. Maak de drone spanningsloos en verwijder propellers als dat veilig kan. "
        "Dit moet door een docent of werkplaatsbegeleider worden beoordeeld. Beschrijf daarna kort wat je ziet: rook, hitte, schade, foutmelding of trilling."
    )
