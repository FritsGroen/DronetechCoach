# DroneTech Coach — starterpakket

Dit starterpakket is bedoeld voor een eerste schoolpilot van een AI-assistent voor drone-techniek.

## Architectuur

- **GitHub Pages** serveert de statische frontend uit de map `/docs`.
- **Mini-pc** draait de Node js backend uit de map `/backend`.
- **Teams** laadt de frontend als tab/tegeltje.
- **OpenAI** wordt alleen vanaf de backend aangeroepen.
- **Kennisbank** staat in `/knowledge`.

## Wat komt waar?

### In GitHub
Zet de **hele repository** in GitHub.

- `/docs` → statische site voor GitHub Pages
- `/backend` → broncode voor de mini-pc
- `/knowledge` → kennisdocumenten en chunk-bestanden
- `/teams-app` → Teams-app package/manifest
- `/tests` → testvragen
- `/scripts` → scripts om de kennisbank opnieuw op te bouwen

### Op de mini-pc
Clone dezelfde repository, bijvoorbeeld naar:

```bash
/opt/dronetech-coach
```

Daar draai je alleen:
- `/backend`
- `/knowledge`
- optioneel `/scripts`

De map `/docs` hoeft op de mini-pc niet actief geserveerd te worden als GitHub Pages dat al doet.

## Snelle start

### 1. Backend lokaal starten
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# vul OPENAI_API_KEY en ALLOWED_ORIGINS in
uvicorn app:app --host 0.0.0.0 --port 8000
```

### 2. Kennischunks opnieuw bouwen
```bash
cd ..
python scripts/chunk_knowledge.py
```

### 3. GitHub Pages instellen
In GitHub:
- ga naar **Settings**
- ga naar **Pages**
- kies branch **main**
- kies folder **/docs**

### 4. Frontend laten wijzen naar je backend
Pas in `/docs/config.js` aan:
```js
window.DRONETECH_CONFIG = {
  API_BASE_URL: "https://jouwdomein.nl/api"
};
```

### 5. Teams manifest invullen
Pas in `/teams-app/manifest.json` aan:
- `id`
- `developer`
- `name`
- `configurationUrl`
- `websiteUrl`
- `validDomains`

Zip daarna alleen deze 3 bestanden voor Teams:
- `manifest.json`
- `color.png`
- `outline.png`
