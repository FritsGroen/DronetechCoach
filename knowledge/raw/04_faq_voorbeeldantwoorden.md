# 4. Veelgestelde vragen en voorbeeldantwoorden — voor studenten en docenten

## Doel
Snelle vraag-antwoordbank voor gebruik in onderwijs, practicumbegeleiding en eerstelijnsondersteuning.

## Gebruik door een Teams-assistent
Gebruik dit document als antwoordbasis bij:
- korte studentvragen;
- terugkerende docentvragen;
- eerste diagnose bij opstart, bouwen of testen.

## Afbakening
Dit document geeft **directe antwoorden**.  
Voor **uitleg van begrippen**: zie document 1.  
Voor **procedures en checklists**: zie document 2.  
Voor **formats**: zie document 3.

---

## 1. Vragen van studenten

### 1. Wat is het verschil tussen een flight controller en een autopilot?
**Voorbeeldantwoord**  
Een flight controller is de rekeneenheid die sensoren uitleest en motoren aanstuurt. Met autopilot bedoelen we meestal de complete besturingslaag: hardware plus firmware plus vliegmodi en failsafes.

### 2. Waarom moet ik vaak zonder propellers beginnen?
**Voorbeeldantwoord**  
Omdat je dan voeding, sensoren, RC, motorrichting en modes kunt controleren zonder direct letsel- of schaderisico. Bench tests doe je daarom standaard zonder propellers.

### 3. Mijn drone wil niet armen. Waar kijk ik eerst?
**Voorbeeldantwoord**  
Kijk eerst naar de pre-arm melding. Controleer daarna throttle-stand, vluchtmodus, sensorstatus, RC-verbinding en eventuele GPS- of failsafe-eisen.

### 4. Waarom trilt mijn drone zo sterk?
**Voorbeeldantwoord**  
Meestal door beschadigde of ongebalanceerde props, een kromme motoras, losse schroeven of een ongunstige montage van de flight controller. Stop met vliegen en controleer eerst mechanisch.

### 5. Wat betekent hover throttle?
**Voorbeeldantwoord**  
Dat is het gasniveau waarbij de drone ongeveer stil in de lucht blijft hangen. Het zegt iets over de vermogensreserve van je systeem.

### 6. Waarom is te weinig throttle reserve ongunstig?
**Voorbeeldantwoord**  
Omdat de drone dan weinig ruimte overhoudt voor correcties bij wind, manoeuvres of storingen. Dat maakt regelen moeilijker en minder veilig.

### 7. Wat is het verschil tussen stabilize, altitude hold en loiter?
**Voorbeeldantwoord**  
Stabilize helpt vooral met houding. Altitude hold probeert hoogte vast te houden. Loiter houdt meestal zowel positie als hoogte ongeveer vast.

### 8. Waarom moet ik sensoren kalibreren?
**Voorbeeldantwoord**  
Omdat sensoren offsets, schaalfouten en richtingsfouten kunnen hebben. Zonder kalibratie worden schatting en regeling onnauwkeurig.

### 9. Wat doet een ESC precies?
**Voorbeeldantwoord**  
Een ESC vertaalt het stuursignaal van de flight controller naar de elektrische aandrijving van een brushless motor. Zonder ESC kan de motor niet correct geregeld worden.

### 10. Mag ik verschillende propellers of motoren mixen?
**Voorbeeldantwoord**  
In onderwijs en basisbouw liever niet. Verschillende karakteristieken maken afregeling, diagnose en veiligheid moeilijker.

### 11. Waarom moet ik logbestanden bewaren?
**Voorbeeldantwoord**  
Omdat logs de snelste manier zijn om achteraf te zien wat de drone, sensoren en besturing deden. Zonder log moet je vaak gokken.

### 12. Wat is het verschil tussen SIL en HIL?
**Voorbeeldantwoord**  
Bij SIL draait alles in software. Bij HIL draait echte flight controllerhardware mee, terwijl de omgeving nog gesimuleerd is. HIL zit dus dichter op de echte praktijk.

### 13. Mijn hoogtehold “pompt”. Wat kan de oorzaak zijn?
**Voorbeeldantwoord**  
Vaak combinatie van agressieve tuning, lawaaiige hoogte-inschatting, trillingen of te grote vertraging in de regelketen. Controleer eerst sensoren en trillingen, daarna tuning.

### 14. Waarom is mijn GPS binnen onbetrouwbaar?
**Voorbeeldantwoord**  
Omdat satellietontvangst binnen zwak of verstoord is. Gebruik binnen liever geen modi die sterk van GPS afhangen, tenzij je een geschikt alternatief hebt.

### 15. Wat moet ik na een harde landing altijd controleren?
**Voorbeeldantwoord**  
Propellers, motorassen, frame, flight controller-montage, accu, kabels en sensoruitlijning. Daarna opnieuw bench testen vóór de volgende vlucht.

---

## 2. Vragen van docenten

### 16. Hoe voorkom ik dat alle studenten hetzelfde opleveren?
**Voorbeeldantwoord**  
Varieer in frameconfiguratie, massa, modelvorm, regelopgave of testcondities. Geef hetzelfde format, maar andere randvoorwaarden of acceptatiecriteria.

### 17. Hoe deel ik een practicum veilig op?
**Voorbeeldantwoord**  
Werk in fasen: theorie en checklist, bench test zonder props, beperkte functietest, indoor test, pas daarna buiten. Laat risicovolle stappen alleen doen als eerdere fases aantoonbaar goed zijn.

### 18. Wat is een goede minimale documentatieset?
**Voorbeeldantwoord**  
PvE, task cards, logboek, acceptatiecriteria en eindreflectie. Daarmee kun je zowel techniek als proces en veiligheid beoordelen.

### 19. Hoe beoordeel ik of een student echt begrijpt wat hij doet?
**Voorbeeldantwoord**  
Vraag niet alleen om een werkend toestel, maar ook om een foutanalyse, onderbouwing van keuzes en uitleg van veiligheidsmaatregelen. Begrip blijkt uit diagnose en argumentatie.

### 20. Hoe ga ik om met grote groepen?
**Voorbeeldantwoord**  
Laat studenten zoveel mogelijk simulatie, bench tests en indoor werk doen. Houd buitenvluchten strak georganiseerd en docent-gestuurd.

### 21. Welke fouten zie je vaak bij beginners?
**Voorbeeldantwoord**  
Props te vroeg monteren, geen vaste checklist gebruiken, polariteit niet dubbelchecken, logboek overslaan, te snel buiten willen vliegen en tuning verwarren met mechanische problemen.

### 22. Wanneer laat ik studenten níet vliegen?
**Voorbeeldantwoord**  
Bij ontbrekende veiligheidscheck, onbekende foutmelding, zichtbare schade, onverklaarde trillingen, twijfel over failsafe of onvoldoende supervisie.

### 23. Hoe maak ik een opdracht passend voor verschillende niveaus?
**Voorbeeldantwoord**  
Gebruik drie treden: basis uitvoeren, analyse aanpassen, ontwerp zelf specificeren. Zo kan één thema toch op meerdere niveaus worden aangeboden.

### 24. Hoe houd ik feedback praktisch?
**Voorbeeldantwoord**  
Geef feedback per categorie: veiligheid, techniek, analyse, documentatie. Vraag steeds om één concrete volgende stap in plaats van een algemeen “verbeter dit”.

### 25. Hoe gebruik ik een Teams-assistent verstandig in het onderwijs?
**Voorbeeldantwoord**  
Laat de assistent vooral helpen bij begrippen, formats, checklists en eerste diagnose. Laat veiligheidskritische beslissingen altijd door een docent of bevoegde begeleider bevestigen.

---

## 3. Korte diagnose-antwoorden voor de assistent

### Vraag: “Motor 3 start later dan de rest. Is dat erg?”
**Antwoordpatroon**  
Ja, dat is relevant. Controleer eerst zonder propellers: motorvolgorde, ESC-signaal, connectoren, kalibratie, wrijving in de motor en schade aan de prop-as. Pas daarna opnieuw testen.

### Vraag: “Mijn drone trekt direct naar één kant.”
**Antwoordpatroon**  
Stop en ga terug naar de werkbank. Controleer propellerrichting, motorrichting, frame-uitlijning, CG, sensororiëntatie en flight controller-montage.

### Vraag: “De accu wordt erg warm.”
**Antwoordpatroon**  
Niet opnieuw vliegen voordat je de oorzaak weet. Mogelijke oorzaken zijn te hoge stroom, verkeerde propellercombinatie, oude accu, slechte connector of te weinig vermogensreserve.

### Vraag: “Kan ik direct buiten testen?”
**Antwoordpatroon**  
Alleen als bench test, modecheck, motorcheck, failsafecheck en liefst een gecontroleerde indoor of tethered test al geslaagd zijn.

### Vraag: “Is een firmware-update altijd slim vlak voor een practicum?”
**Antwoordpatroon**  
Nee. Vlak voor een les of test wil je stabiliteit. Update alleen gecontroleerd, documenteer wijzigingen en herhaal daarna de volledige basiscontrole.

---

## 4. Antwoordstijl voor studenten
Gebruik dit patroon:
1. direct antwoord;
2. belangrijkste reden;
3. veiligste eerstvolgende stap;
4. verwijs zo nodig naar document 2 of 3.

**Voorbeeld**  
“Ja, je moet opnieuw kalibreren na een andere sensoropstelling. Anders klopt je referentie niet meer. Verwijder eerst de propellers en herhaal daarna de sensor- en modecheck.”

---

## 5. Antwoordstijl voor docenten
Gebruik dit patroon:
1. didactisch advies;
2. veiligheidsgrens;
3. minimaal bewijs of documentatie;
4. schaalbare werkvorm.

**Voorbeeld**  
“Laat studenten eerst in tweetallen een bench test aftekenen. Geen props vóór de check compleet is. Vraag om logboek plus screenshot van systeemstatus. Laat buitenvluchten alleen in blokken onder docenttoezicht plaatsvinden.”

---

## 6. Escalatieregels voor de Teams-assistent
De assistent moet **niet** doen alsof elke vraag op afstand veilig op te lossen is. Escaleer naar docent/werkplaatsbegeleider bij:
- rook, hitte of elektrische schade;
- crash of harde landing;
- terugkerende arming-problemen zonder duidelijke melding;
- ernstige trillingen;
- twijfel over veilige vliegcondities;
- vragen met directe letsel- of aansprakelijkheidsrisico’s.

---

## 7. Taalregels voor de Teams-assistent
- Geen lange theorie als iemand om een snelle oplossing vraagt.
- Noem altijd de veiligste stap eerst.
- Vermijd absolute zekerheid bij onvolledige diagnose.
- Sluit af met één concreet vervolg.

---

## Bronbasis
Gebaseerd op de in de bronset beschreven componenten, testfasen, regel- en failsafe-logica, plus algemene onderwijs- en werkplaatsvragen uit dronepraktijk.
