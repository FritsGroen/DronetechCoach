# 2. Bouw, onderhoud en checklists — Drone-techniek

## Doel
Werkdocument voor opbouw, configuratie, onderhoud en operationele controles van een multicopter.

## Gebruik door een Teams-assistent
Gebruik dit document voor vragen als:
- “Waar begin ik met bouwen?”
- “Welke controles doe ik vóór de eerste vlucht?”
- “Wat controleer ik na een crash?”
- “Hoe houd ik onderhoud bij?”

## Afbakening
Dit document beschrijft **wat je doet en controleert**.  
Voor **definities en theorie**: zie document 1.  
Voor **onderwijsformats**: zie document 3.  
Voor **FAQ’s en voorbeeldantwoorden**: zie document 4.

---

## 1. Ontwerpvolgorde in 8 stappen
1. **Bepaal missie en randvoorwaarden**  
   Payload, gewenste vliegtijd, maximale afmeting, binnen/buiten, veiligheidsniveau.
2. **Kies frame en propellerklasse**  
   Grootte moet passen bij propellers, elektronica en payload.
3. **Kies motoren**  
   Voldoende stuwkracht, thermische marge en passende KV.
4. **Kies ESC’s**  
   Stroommarge, protocolcompatibiliteit en koeling.
5. **Kies accu**  
   Spanning, capaciteit, massa, connector en ontlaadvermogen.
6. **Kies flight controller en firmware**  
   Passend bij sensoren, poorten, gewenste modi en onderwijsdoel.
7. **Kies besturings- en dataomgeving**  
   Zender, ontvanger, telemetrie, ground station, logging.
8. **Plan testopbouw**  
   Bench test → simulatie/HIL → indoor → buiten.

---

## 2. Compatibiliteitsregels

### 2.1 Mechanisch
- Propellers mogen elkaar of frameonderdelen nooit kunnen raken.
- Flight controller moet trillingsarm en logisch georiënteerd gemonteerd zijn.
- Accu moet stevig vastzitten en snel te verwijderen zijn.
- Kabels moeten vrij liggen van propellers en scharnierpunten.

### 2.2 Elektrisch
- Polariteit altijd dubbel controleren vóór eerste power-on.
- Connectoren moeten passen bij verwachte stroom.
- ESC-continuestroom moet boven realistische piekbelasting liggen.
- Voedingspaden voor flight controller en randapparatuur moeten bekend zijn.

### 2.3 Logisch/softwarematig
- Airframe-configuratie moet overeenkomen met het echte frame.
- Motorvolgorde en draairichting moeten overeenkomen met firmware-instellingen.
- RC-kanalen moeten logisch gemapt zijn.
- Vliegmodi en failsafes moeten vóór de eerste propeller-run getest zijn.

---

## 3. Bouwchecklist

### 3.1 Mechanische opbouw
- [ ] Frame recht en torsiestijf opgebouwd
- [ ] Schroeven met passende lengte en borging gebruikt
- [ ] Motoren vlak en stevig bevestigd
- [ ] Prop-adapters/spinners correct gemonteerd
- [ ] Flight controller trillingsarm gemonteerd
- [ ] GPS/magnetometer vrij van sterke stroombronnen geplaatst
- [ ] Ontvangerantennes vrij en logisch georiënteerd
- [ ] Accuband en antislip aanwezig
- [ ] Landingsgestel stabiel

### 3.2 Elektrische opbouw
- [ ] Hoofdvoedingspad gecontroleerd op polariteit
- [ ] Soldeerverbindingen mechanisch sterk en elektrisch schoon
- [ ] Geen blanke aders zichtbaar
- [ ] Krimpkous of isolatie op alle risicopunten
- [ ] ESC-signaalkabels correct aangesloten
- [ ] Eventuele BEC/regelvoeding passend gekozen
- [ ] Telemetrie, GPS en extra sensoren op juiste poorten

### 3.3 Logische opbouw
- [ ] Juiste frame type geselecteerd
- [ ] Juiste mixer/configuratie actief
- [ ] Motorvolgorde gecontroleerd
- [ ] Draairichting motoren gecontroleerd
- [ ] Juiste props op juiste motoren geplaatst
- [ ] RTL/home/failsafe-parameters ingevuld
- [ ] Logging ingeschakeld

---

## 4. Eerste opstart zonder propellers
**Altijd eerst zonder propellers.**

1. Visuele inspectie
2. Power-on met rook-/kortsluitbewustzijn
3. Controleer op onverwachte warmte
4. Verbind met configuratiesoftware
5. Controleer sensorstatus
6. Controleer RC-ingangen
7. Controleer motor-outputvolgorde zonder propellers
8. Controleer richting van elk motorcommando
9. Test arm/disarm
10. Test failsafe-reacties op een veilige manier

---

## 5. Kalibratievolgorde
Aanbevolen volgorde:
1. firmware en frameconfiguratie;
2. accelerometer/IMU;
3. kompas indien aanwezig en zinvol;
4. RC-kalibratie;
5. vluchtmodi;
6. failsafes;
7. ESC/motor-outputcontrole;
8. logging en telemetrie;
9. indoor hovertest;
10. pas daarna buiten vliegen.

---

## 6. Bench test checklist
- [ ] Propellers verwijderd
- [ ] Werkplek vrij van metalen rommel en losse kabels
- [ ] Veilige voeding aangesloten
- [ ] Flight controller start zonder foutmeldingen
- [ ] Sensorwaarden plausibel
- [ ] RC-input correct
- [ ] Flight modes schakelen correct
- [ ] Telemetrie/logging werkt
- [ ] Motors reageren in juiste volgorde
- [ ] Noodstop of snelle disarm bekend en getest

---

## 7. Pre-flight checklist
Gebruik vóór elke vlucht een vaste routine.

### 7.1 Omgeving
- [ ] Vlieggebied is toegestaan en veilig
- [ ] Voldoende afstand tot mensen, dieren, voertuigen en obstakels
- [ ] Wind en zichtcondities passen bij toestel en piloot
- [ ] Start- en landingszone vrij
- [ ] Home-positie logisch gekozen

### 7.2 Drone
- [ ] Frame zonder scheuren of speling
- [ ] Propellers onbeschadigd en correct vast
- [ ] Accu mechanisch goed vastgezet
- [ ] Kabels niet in propellerbaan
- [ ] Sensoren vrij en schoon
- [ ] Antennes correct geplaatst
- [ ] CG acceptabel

### 7.3 Systeemstatus
- [ ] Voldoende accuspanning
- [ ] GPS-lock indien nodig
- [ ] Geen kritieke waarschuwingen
- [ ] Juiste vliegmodus voor de start
- [ ] RTL/failsafe geverifieerd
- [ ] Piloot kent noodprocedure

### 7.4 Team
- [ ] Rollen afgesproken: piloot, spotter, observator
- [ ] Commando’s afgesproken
- [ ] Abort-criteria uitgesproken

---

## 8. Startprocedure
1. Plaats drone stabiel en vrij.
2. Zet zender aan vóór de drone als dat je procedure is.
3. Sluit accu aan en wacht op complete initialisatie.
4. Controleer armstatus, vluchtmodus en waarschuwingen.
5. Laatste visuele check van props en omgeving.
6. Arm bewust, niet automatisch.
7. Stijg beheerst op naar veilige controlehoogte.
8. Controleer eerst stabiliteit, respons en geluid.
9. Pas daarna missie of verdere test.

---

## 9. Post-flight checklist
- [ ] Direct disarmen
- [ ] Accu loskoppelen
- [ ] Temperatuur van motoren, ESC’s en accu voelen
- [ ] Props inspecteren op chips of kromming
- [ ] Frame en landing gear controleren
- [ ] Logbestanden veiligstellen
- [ ] Bijzonderheden noteren
- [ ] Accu op juiste opslag- of laadroute zetten

---

## 10. Onderhoudsschema

### Na elke vlucht
- schoonmaken;
- props, frame en kabels inspecteren;
- bijzonderheden loggen;
- accu beoordelen op zwelling, schade en spanning.

### Wekelijks of na intensief gebruik
- schroefverbindingen nalopen;
- motorlagers/speling controleren;
- trillingsbronnen opsporen;
- antenne- en connectorconditie controleren;
- firmware-instellingen en logging beoordelen.

### Na harde landing of crash
- propellers vervangen of afzonderlijk vrijgeven na inspectie;
- motoras op slingering controleren;
- frame op haarscheuren inspecteren;
- flight controller-montage opnieuw controleren;
- sensor- en GPS-mast uitlijning controleren;
- volledige bench test opnieuw uitvoeren.

---

## 11. Accubeheer
- Gebruik alleen onbeschadigde LiPo’s.
- Laad met passend laadprogramma.
- Laat accu’s niet warm wegleggen in gesloten tas.
- Bewaar accu’s op opslagspanning.
- Markeer oude of verdachte accu’s direct.
- Gebruik een eenduidig accusysteem met ID, aantal cycli en status.

### Minimale accuregistratie
| Accu-ID | Type | Capaciteit | Cycli | Laatste vlucht | Status |
|---|---|---:|---:|---|---|
| B01 | 4S LiPo | 5200 mAh | 18 | 2026-04-03 | OK / observeren / afkeuren |

---

## 12. Veilige testopbouw voor onderwijs
1. **Simulatie of paper check**
2. **Bench test zonder propellers**
3. **Motor test met beperkte risico’s**
4. **Indoor of tethered test**
5. **Buitenproef met kleine envelope**
6. **Pas daarna volledige opdracht**

Didactisch is dit sterk, omdat fouten vroeg zichtbaar worden en schade klein blijft.

---

## 13. Snelle foutsignalen die directe stop rechtvaardigen
- onverwachte rook, geur of hitte;
- sterke trillingen;
- duidelijk asymmetrisch motorgeluid;
- onverklaarbare sensorfouten;
- wegvallende RC-link;
- onlogische modewissels;
- zichtbaar beschadigde propeller of loszittende accu.

Bij één van deze signalen: **niet doorvliegen**.

---

## 14. Beslisboom voor de werkbank
**Drone start niet goed op**
1. Krijgt de flight controller voeding?
2. Is polariteit correct?
3. Is de firmware/configuratie passend?
4. Werkt verbinding met GCS?
5. Zijn RC en sensoren zichtbaar?

**Drone armt niet**
1. Welke pre-arm melding zie je?
2. Is de gekozen modus toegestaan?
3. Is throttle laag?
4. Zijn GPS/kompas-eisen passend voor deze situatie?
5. Is failsafe of geofence actief?

**Drone trilt te veel**
1. Props beschadigd?
2. Motoras recht?
3. Schroeven los?
4. Flight controller te stijf of juist te slap gemonteerd?
5. Propellercombinatie passend?

---

## 15. Minimale onderhoudslog
| Datum | Toestel | Uren/vluchten | Bevinding | Actie | Uitvoerder |
|---|---|---:|---|---|---|
| 2026-04-03 | F450-01 | 12 vluchten | Prop 2 kleine chip | vervangen | docent A |

---

## 16. Taalregels voor een Teams-assistent
Bij procedurevragen:
1. Begin met de **veiligste eerstvolgende stap**.
2. Werk daarna in korte volgorde.
3. Noem expliciet of propellers eraf moeten.
4. Sluit af met “controleer logboek/FAQ” als vervolg.

---

## Bronbasis
Gebaseerd op multicopter opbouw, airframe- en propulsieontwerp, Pixhawk-configuratie, HIL-teststappen en failsafe-principes uit de aangeleverde bronset, aangevuld met algemene werkplaats- en vliegveiligheidspraktijk.
