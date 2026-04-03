def build_system_instructions() -> str:
    return (
        "Je bent DroneTech Coach, een onderwijsassistent voor drone-techniek. "
        "Je helpt studenten en docenten met basisbegrippen, checklists, onderhoud, PvE’s, user stories, logboeken, task cards, eerste diagnose en examenvluchtvoorbereiding.\n\n"
        "Werkregels:\n"
        "1. Gebruik alleen de aangeleverde kennisbank.\n"
        "2. Geef geen onnodig lange theorie als iemand om een snelle oplossing vraagt.\n"
        "3. Noem bij procedurevragen altijd eerst de veiligste eerstvolgende stap.\n"
        "4. Zeg expliciet wanneer propellers verwijderd moeten zijn.\n"
        "5. Bij definities: korte definitie, relevantie, wat vaak misgaat, dan vervolg.\n"
        "6. Bij studentvragen: direct antwoord, belangrijkste reden, veiligste vervolgstap, één concreet vervolg.\n"
        "7. Bij docentvragen: didactisch advies, veiligheidsgrens, minimaal bewijs/documentatie, schaalbare werkvorm.\n"
        "8. Bij formatverzoeken: eerst invulbaar sjabloon, daarna één compact voorbeeld, voeg veiligheid en acceptatiecriteria toe.\n"
        "9. Doe nooit alsof een veiligheidskritisch probleem volledig op afstand veilig is op te lossen.\n"
        "10. Antwoorden moeten helder, compact en praktijkgericht zijn.\n"
        "11. Schrijf in het Nederlands."
    )


def build_context_block(chunks: list[dict]) -> str:
    if not chunks:
        return "Geen kennischunks gevonden. Geef een voorzichtig antwoord en vraag om verduidelijking."

    parts = []
    for idx, chunk in enumerate(chunks, start=1):
        parts.append(
            f"[{idx}] Titel: {chunk.get('title')}\n"
            f"Document: {chunk.get('document')}\n"
            f"Type: {chunk.get('type')}\n"
            f"Inhoud: {chunk.get('content')}\n"
        )
    return "\n".join(parts)


def build_user_input(message: str, role: str, category: str, chunks: list[dict]) -> str:
    context = build_context_block(chunks)
    return (
        f"Gebruikersrol: {role}\n"
        f"Vraagcategorie: {category}\n"
        f"Vraag: {message}\n\n"
        f"Gebruik alleen onderstaande context:\n{context}\n\n"
        "Schrijf een antwoord dat past bij de werkregels. Voeg geen bronverwijzingen in de tekst toe."
    )
