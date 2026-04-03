# 3. Onderwijsformats — PvE, user stories, logboeken en task cards

## Doel
Compact formatdocument voor onderwijs, practica, projecten en toetsing in drone-techniek.

## Gebruik door een Teams-assistent
Gebruik dit document voor vragen als:
- “Heb je een PvE-format voor een droneproject?”
- “Maak een user story voor een hoogtehoudfunctie.”
- “Hoe ziet een logboek eruit?”
- “Kun je een task card voor sensorcalibratie geven?”

## Afbakening
Dit document bevat **formats en invulstructuren**.  
Voor **theorie en definities**: zie document 1.  
Voor **bouw- en onderhoudsstappen**: zie document 2.  
Voor **veelgestelde vragen en voorbeeldantwoorden**: zie document 4.

---

## 1. Ontwerprichtlijn voor onderwijs
Gebruik bij drone-opdrachten drie niveaus:
1. **Basis** — herhalen, uitvoeren, waarnemen
2. **Analyse** — aanpassen, meten, vergelijken
3. **Ontwerp** — zelf specificeren, bouwen, valideren

Dit sluit goed aan op dronepraktijk: eerst begrijpen, dan wijzigen, dan ontwerpen.

---

## 2. PvE-format (Programma van Eisen)

## 2.1 Sjabloon
**Projecttitel**  
**Versie**  
**Team / student**  
**Datum**

### A. Doel van het systeem
- Welke taak moet de drone uitvoeren?
- Voor welke gebruiker of situatie?
- Waarom is dit project relevant?

### B. Functionele eisen
- De drone moet …
- De operator moet …
- Het systeem moet kunnen schakelen tussen …

### C. Prestatie-eisen
- Maximale massa:
- Minimale vliegtijd:
- Minimale payload:
- Maximale afmeting:
- Gewenste nauwkeurigheid:
- Reactietijd / settling:
- Maximale windsituatie:

### D. Veiligheidseisen
- Failsafe bij RC-verlies:
- Failsafe bij lage accu:
- Maximaal risiconiveau:
- Testopbouw:
- Geofence / no-go zones:

### E. Technische randvoorwaarden
- Flight controller / firmware:
- Sensoren:
- Simulatie-eis:
- Logverplichting:
- Telemetrie ja/nee:

### F. Onderwijs- en oplevereisen
- Op te leveren documenten:
- Demonstratie:
- Broncode / model:
- Presentatie:
- Reflectie:

### G. Acceptatiecriteria
- Het systeem is acceptabel als …
- De test is geslaagd wanneer …
- De veiligheidscheck is voldaan wanneer …

## 2.2 Voorbeeld-PvE
**Project**: Quadcopter met hoogtehoudfunctie voor practicum  
**Doel**: stabiel hoveren op één hoogte gedurende 20 seconden  
**Prestatie**: vliegtijd minimaal 8 minuten, hover stabiel binnen ±0,5 m  
**Veiligheid**: props pas monteren na bench test, failsafe = autoland  
**Acceptatie**: indoor test slaagt in 3 opeenvolgende pogingen

---

## 3. User story format

## 3.1 Sjabloon
**Als** [rol]  
**wil ik** [functie of gedrag]  
**zodat** [waarde of doel].

### Acceptatiecriteria
- Gegeven …
- Wanneer …
- Dan …

### Technische notities
- Sensoren:
- Modi:
- Failsafes:
- Logdata:
- Testconditie:

## 3.2 Voorbeelden
### Voorbeeld 1 — student
Als **student drone-techniek**  
wil ik **een duidelijke pre-flight checklist**  
zodat **ik fouten vóór het opstijgen vind**.

Acceptatiecriteria:
- Gegeven een klaarstaande drone,
- wanneer de student de checklist stap voor stap doorloopt,
- dan worden accu, props, mode en failsafe aantoonbaar gecontroleerd.

### Voorbeeld 2 — operator
Als **operator**  
wil ik **met één schakelaar kunnen wisselen tussen stabilize, altitude hold en loiter**  
zodat **ik veilig kan opschalen van handmatig naar semi-autonoom**.

### Voorbeeld 3 — docent
Als **docent**  
wil ik **verschillende ontwerpopgaven per student kunnen uitdelen**  
zodat **studenten zelfstandig ontwerpen en niet allemaal hetzelfde inleveren**.

---

## 4. Format voor acceptance criteria
Gebruik maximaal 5–7 criteria per taak.

| Nr | Criterium | Meetwijze | Geslaagd wanneer |
|---|---|---|---|
| AC1 | Drone start correct op | Bench test | geen kritieke foutmelding |
| AC2 | RC-input klopt | kanaaltest | alle assen correct |
| AC3 | Hoogtehold werkt | indoor test | hoogte blijft binnen band |
| AC4 | Logging draait | logcontrole | bestand aanwezig en leesbaar |

---

## 5. Logboekformat student

## 5.1 Kort format per sessie
**Datum**  
**Team / student**  
**Toestel / configuratie**  
**Doel van de sessie**  
**Uitgevoerde stappen**  
**Waarnemingen**  
**Problemen**  
**Oorzaken (vermoed)**  
**Acties voor volgende keer**  
**Veiligheidsopmerkingen**

## 5.2 Aanbevolen invulregels
- Noteer feiten vóór interpretaties.
- Gebruik meetwaarden waar mogelijk.
- Schrijf ook mislukte tests op.
- Noteer wat is gewijzigd sinds de vorige sessie.
- Sluit af met één concrete volgende stap.

## 5.3 Voorbeeld logboekitem
**Doel**: hoogtehold testen na nieuwe PID-instelling  
**Uitgevoerde stappen**: sensorcheck, RC-check, indoor hovertest  
**Waarnemingen**: hover stabieler dan vorige sessie, maar nog lichte verticale pompbeweging  
**Problemen**: oscillatie bij snelle throttlewissel  
**Volgende stap**: kleine verlaging van P en herhaal test  
**Veiligheid**: props na test direct verwijderd voor bench-analyse

---

## 6. Logboekformat docent
**Klas / groep**  
**Onderdeel / les**  
**Leerdoel**  
**Wat ging goed**  
**Veelvoorkomende fouten**  
**Veiligheidsmomenten**  
**Beslissing voor volgende les**  
**Benodigde materialen**

Dit helpt bij herhaalbaarheid en overdracht tussen docenten.

---

## 7. Task card format

## 7.1 Standaardsjabloon
**Taaknaam**  
**Code**  
**Niveau**: basis / analyse / ontwerp  
**Duur**  
**Benodigdheden**  
**Veiligheidswaarschuwing**  
**Uit te voeren stappen**  
**Op te leveren bewijs**  
**Beoordelingspunten**  
**Stopcriterium**

## 7.2 Voorbeeld task card — sensorcalibratie
**Taaknaam**: IMU-basiscontrole en calibratie  
**Code**: TC-SENS-01  
**Niveau**: basis  
**Duur**: 20 min  
**Benodigdheden**: flight controller, laptop, configuratiesoftware  
**Veiligheid**: propellers verwijderd  
**Stappen**:
1. Verbind flight controller
2. Controleer sensorstatus
3. Voer accelerometercalibratie uit
4. Sla instellingen op
5. Controleer resultaat

**Bewijs**:
- screenshot sensorstatus
- korte reflectie: wat was afwijkend?

**Stopcriterium**:
- onverklaarbare sensorfout;
- instabiele voeding;
- kalibratie mislukt.

## 7.3 Voorbeeld task card — pre-flight
**Taaknaam**: pre-flight inspectie  
**Code**: TC-OPS-01  
**Niveau**: basis  
**Duur**: 10 min  
**Bewijs**: afgetekende checklist + mondelinge toelichting

---

## 8. Experimentkaart
Handig voor practica.

**Titel experiment**  
**Onderzoeksvraag**  
**Hypothese**  
**Onafhankelijke variabele**  
**Afhankelijke variabele**  
**Meetmethode**  
**Veiligheidsmaatregelen**  
**Verwachte uitkomst**  
**Reflectie**

### Voorbeeld
Onderzoeksvraag: wat is het effect van extra massa op hover throttle en vliegtijd?

---

## 9. Beoordelingsrubric compact
| Aspect | Onvoldoende | Voldoende | Goed |
|---|---|---|---|
| Veilig werken | checklists genegeerd | basischecks uitgevoerd | zelfstandig en consequent veilig |
| Technische uitvoering | veel fouten, geen diagnose | systeem werkt deels | werkt stabiel en reproduceerbaar |
| Analyse | losse observaties | redelijke verklaring | meetgegevens, vergelijking en conclusies |
| Documentatie | onvolledig | bruikbaar | helder, volledig en overdraagbaar |

---

## 10. Lesvoorbereidingskaart voor docenten
**Leerdoel**  
**Voorkennis vereist**  
**Benodigd materiaal**  
**Risico’s**  
**Demo door docent**  
**Zelfstandige studenttaak**  
**Meet-/beoordelmoment**  
**Nazorg / huiswerk**

---

## 11. Naamgevingsconventie voor bestanden
Aanbevolen patroon:
`[groep]_[onderwerp]_[versie]_[datum]`

Voorbeelden:
- `T2_preflight_v1_2026-04-03`
- `G1_hoogtehold_logboek_v2_2026-04-03`
- `D5_PvE_multicopter_v1_2026-04-03`

Dit maakt kennisbankbeheer en terugvinden eenvoudiger.

---

## 12. Minimale set voor een compleet studentproject
1. PvE
2. minimaal 3 user stories
3. task cards per praktijksessie
4. logboek per sessie
5. acceptatiecriteria
6. eindreflectie met veiligheidsanalyse

---

## 13. Taalregels voor een Teams-assistent
Bij verzoeken om een format:
1. Geef eerst een **invulbaar sjabloon**
2. Geef daarna **één compact voorbeeld**
3. Houd velden kort en toetsbaar
4. Voeg altijd **veiligheid** en **acceptatiecriteria** toe

---

## Bronbasis
Gebaseerd op de in de bronset beschreven experimentele opbouw basis–analyse–ontwerp, HIL/SIL-werkwijze, docentdifferentiatie en open experimentvormen, aangevuld met praktische onderwijsontwerpervaring voor droneprojecten.
