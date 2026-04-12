# DroneTech Coach

DroneTech Coach is een kennisbot voor Microsoft Teams en GitHub Pages.  
Gebruikers kunnen vragen stellen over dronetechniek, lesmateriaal, projectdocumentatie, checklists en andere kennisbestanden.  
De frontend draait als webpagina / Teams-tab en de backend draait met **Node.js**.

---

## Wat doet deze app?

De app bestaat uit 2 delen:

### 1. Frontend
De frontend is de chatinterface die de gebruiker ziet.

Functies:
- vragen stellen aan de kennisbot
- nieuwe chat starten
- nette weergave van antwoorden
- formuleweergave met KaTeX
- laadanimatie met drone-loader
- bruikbaar in browser én in Microsoft Teams

De frontend kan gehost worden op:
- **GitHub Pages**
- of een andere statische webhost

### 2. Backend
De backend draait lokaal of op een server met **Node.js**.

Taken van de backend:
- ontvangen van vragen uit de frontend
- inlezen van kennisbestanden uit de knowledge-map
- relevante informatie ophalen uit documenten
- de vraag samen met context naar OpenAI sturen
- het antwoord teruggeven aan de frontend

De backend draait meestal op:
- `http://localhost:3000`

Als de backend van buitenaf bereikbaar moet zijn, kan dat via:
- **ngrok**

---

## Hoe werkt het in de praktijk?

De stroom is als volgt:

1. Een gebruiker opent DroneTech Coach in Teams of in de browser.
2. De gebruiker stelt een vraag.
3. De frontend stuurt die vraag naar de Node-backend.
4. De backend zoekt in de map met kennisbestanden.
5. De backend bouwt context op uit de gevonden informatie.
6. De backend stuurt de vraag + context naar OpenAI.
7. Het antwoord komt terug naar de frontend.
8. De gebruiker ziet het antwoord in de chat.

Kort gezegd:

**Frontend → Node backend → knowledge-bestanden + OpenAI → antwoord terug**

---

## Techniek

### Gebruikte stack
- **Node.js**
- **Express**
- **OpenAI API**
- **GitHub Pages** voor de frontend
- **Microsoft Teams tab** voor gebruik binnen Teams
- **ngrok** om de lokale backend extern bereikbaar te maken
- **KaTeX** voor formuleweergave

---

## Projectstructuur

Een mogelijke structuur van het project:

```text
DroneTech-Coach/
│
├── index.html              # frontend
├── server.js               # Node backend
├── package.json
├── package-lock.json
├── .env                    # API keys en instellingen
├── knowledge/              # kennisbestanden
│   ├── pdf/
│   ├── docx/
│   ├── pptx/
│   └── txt/
├── privacy.html
├── terms.html
├── manifest.json           # Teams app manifest
└── icons/
    ├── color.png
    └── outline.png
