# Architectuur

## Frontend
- draait statisch op GitHub Pages
- gebruikt alleen HTML, CSS en JavaScript
- verstuurt vragen naar de backend via `/ask`

## Backend
- draait op de mini-pc
- roept OpenAI aan
- haalt kennischunks op uit `/knowledge/chunks`
- hanteert veiligheidsregels vóór het model antwoordt

## Teams
- laadt de frontend als tab
- gebruikers hoeven niets lokaal te installeren

## Kennisbank
- raw markdown in `/knowledge/raw`
- chunk-bestanden in `/knowledge/chunks`
- opnieuw opbouwen via `/scripts/chunk_knowledge.py`
