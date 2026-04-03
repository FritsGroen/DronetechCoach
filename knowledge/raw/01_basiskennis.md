# 1. Basiskennis en definities — Drone-techniek

## Doel
Compact naslagdocument voor begrippen, systeemonderdelen en kernconcepten in drone-techniek.

## Gebruik door een Teams-assistent
Gebruik dit document voor vragen als:
- “Wat is een ESC?”
- “Wat is het verschil tussen stabiliseren en positioneren?”
- “Wat betekent failsafe of RTL?”
- “Wat is het verschil tussen SIL en HIL?”

## Afbakening
Dit document legt uit **wat iets is**.  
Voor **bouwstappen en checklists**: zie document 2.  
Voor **onderwijsformats**: zie document 3.  
Voor **FAQ’s en voorbeeldantwoorden**: zie document 4.

---

## 1. Systeembeeld van een multicopter
Een multicopter is een luchtvaartuig met drie of meer aangedreven rotoren. De meest gebruikte vorm is de quadcopter. Het systeem bestaat meestal uit:
1. **Airframe** — frame, armen, landingsgestel, montagepunten.
2. **Propulsiesysteem** — motoren, propellers, ESC’s en accu.
3. **Besturing** — flight controller/autopilot, sensoren, firmware.
4. **Mens-machine-interface** — zender/ontvanger, ground control station, telemetrie.
5. **Missielast** — camera, meetapparatuur, grijper of andere payload.

Een drone is in de praktijk pas bruikbaar als deze vijf delen logisch samenwerken.

---

## 2. Hoofdonderdelen en definities

### 2.1 Airframe
**Airframe**: het dragende mechanische deel van de drone.  
Belangrijke eigenschappen:
- stijf genoeg om trillingen te beperken;
- licht genoeg om efficiënt te vliegen;
- groot genoeg voor propellers, elektronica en payload;
- robuust genoeg voor veilig testen.

### 2.2 Propeller
**Propeller**: draaivleugel die lucht versnelt en zo stuwkracht opwekt.  
Belangrijke begrippen:
- **diameter**: totale maat van tip tot tip;
- **pitch**: theoretische verplaatsing per omwenteling;
- **CW/CCW**: rechts- of linksdraaiende propeller;
- **balans**: onbalans geeft trillingen, slechtere sensordata en extra slijtage.

### 2.3 Motor
**Brushless motor**: elektromotor voor propelleraandrijving.  
Belangrijke begrippen:
- **KV-waarde**: globale maat voor toerental per volt zonder belasting;
- **maximale continue stroom**: stroom die de motor veilig kan verdragen;
- **koppel**: draaikracht van de motor;
- **temperatuurreserve**: praktische marge om oververhitting te voorkomen.

### 2.4 ESC
**ESC (Electronic Speed Controller)**: regelaar tussen accu, flight controller en motor.  
Taken:
- zet stuursignalen om in motoraansturing;
- levert drie-fase aandrijving aan de motor;
- kan extra functies hebben zoals telemetry, remmen of protocolondersteuning.

### 2.5 Accu
**LiPo-accu**: veelgebruikte energiebron voor multicopters.  
Belangrijke begrippen:
- **S-aantal**: aantal cellen in serie, bepaalt de nominale spanning;
- **capaciteit (mAh)**: opgeslagen lading;
- **C-rate**: maat voor maximale ontlaadsnelheid;
- **spanningszak**: spanningsdaling onder belasting;
- **opslagspanning**: veilige spanning voor bewaren.

### 2.6 Flight controller / autopilot
**Flight controller**: rekeneenheid die sensordata verwerkt en stuurcommando’s naar motoren stuurt.  
**Autopilot**: flight controller plus firmwarelogica voor stabilisatie, navigatie en failsafe-gedrag.

### 2.7 Sensoren
Veelgebruikte sensoren:
- **IMU**: combinatie van gyroscoop en versnellingsmeter;
- **magnetometer**: richtingsinformatie;
- **barometer**: hoogte-inschatting via luchtdruk;
- **GPS/GNSS**: positie, snelheid en tijd;
- **afstandssensor / vision sensor**: lokale hoogte- of positieondersteuning.

### 2.8 RC-systeem
**RC-zender**: handzender van de piloot.  
**RC-ontvanger**: ontvangt signalen en geeft deze door aan de flight controller.  
Doel: directe handmatige input of modekeuze.

### 2.9 GCS en telemetrie
**Ground Control Station (GCS)**: software voor configuratie, monitoring en mission management.  
**Telemetrie**: draadloze datalink tussen drone en grondstation.

### 2.10 Payload
**Payload**: de nuttige last die niet nodig is om te vliegen, maar wel voor de taak.  
Voorbeelden: camera, multisensor, luidspreker, pick-up mechanisme, meetinstrument.

---

## 3. Vliegen en regelen

### 3.1 Stuwkracht en momenten
Een multicopter bestuurt zichzelf door verschillen in motortoerental. Daarmee ontstaan:
- **totale stuwkracht** voor op- en neergaan;
- **rolmoment** voor links/rechts kantelen;
- **pitchmoment** voor voorover/achterover kantelen;
- **yawmoment** voor draaien om de verticale as.

### 3.2 Hover
**Hover**: stationair vliegen met netto verticale kracht ongeveer nul.  
Praktisch wil je hover niet te dicht bij vol gas hebben. Een werkbare reserve is nodig voor:
- correcties bij wind;
- manoeuvres;
- veilige regeling.

### 3.3 Attitude, rate en positie
- **Rate control**: regelt draaisnelheid.
- **Attitude control**: regelt hoekstand.
- **Altitude control**: regelt hoogte.
- **Position control**: regelt horizontale positie.
- **Navigation / guidance**: bepaalt waar de drone heen moet.

### 3.4 Control loop
Een **control loop** meet de toestand, vergelijkt die met een gewenste waarde en corrigeert de actuatoren.  
Typisch gelaagd:
1. snelle binnenlus: rates;
2. middenlus: attitude;
3. buitenlus: hoogte of positie.

### 3.5 Dead zone
**Dead zone**: gebied rond de middenstand van een stick waarin kleine invoer niet direct tot commandoverandering leidt. Handig voor stabiel hoveren.

---

## 4. Kalibratie, schatting en tuning

### 4.1 Kalibratie
**Kalibratie**: het meten en corrigeren van offsets, schaalfouten of richtingsfouten van sensoren en invoerapparatuur.  
Voorbeelden:
- accelerometerkalibratie;
- kompascalibratie;
- RC-kalibratie;
- ESC/motor-richtingcontrole.

### 4.2 State estimation
**State estimation**: schatten van houding, snelheid en positie uit meerdere sensoren.  
Waarom nodig:
- ruwe sensoren zijn ruisachtig;
- geen enkele sensor vertelt het hele verhaal;
- regelsystemen hebben stabiele toestandsinformatie nodig.

### 4.3 Filter
**Complementary filter**: combineert snel maar driftgevoelig gedrag met langzamer maar stabieler gedrag.  
**Kalman-filter / EKF**: modelgebaseerde schatter die met ruis en onzekerheid omgaat.

### 4.4 Tuning
**Tuning**: het afregelen van regelparameters zodat het systeem snel, stabiel en veilig reageert.  
Te agressief afgestemd geeft vaak oscillaties; te traag afgestemd geeft slappe of onnauwkeurige besturing.

---

## 5. Bedrijfsmodi en automatisering

### 5.1 Handmatig, semi-autonoom en autonoom
- **Handmatig**: piloot stuurt direct.
- **Semi-autonoom**: piloot geeft commando’s, autopilot stabiliseert of houdt hoogte/positie vast.
- **Autonoom**: systeem volgt zelf een taak of missie.

### 5.2 Veelgebruikte vliegmodi
- **Stabilize**: attitudehulp, positie niet automatisch vast.
- **Altitude Hold / AltHold**: hoogte wordt actief bewaakt.
- **Loiter / Position Hold**: hoogte en positie blijven ongeveer behouden.
- **RTL (Return to Launch)**: terug naar home-positie en daarna landen of wachten.
- **Auto Land**: automatische landing.
- **Mission / Auto**: volgt vooraf ingestelde waypoints of logica.

### 5.3 Home-positie
**Home**: referentiepunt voor RTL en veiligheidslogica. Meestal vastgelegd bij arm of bij GPS-lock.

---

## 6. Veiligheid en failsafes

### 6.1 Arm en disarm
- **Armen**: motorsysteem vrijgeven.
- **Disarmen**: motorsysteem veilig uitschakelen.

### 6.2 Failsafe
**Failsafe**: vooraf gedefinieerde reactie op een fout of verlies van informatie.  
Voorbeelden:
- verlies van RC-link;
- GPS-storing;
- kompasfout;
- accuspanning te laag;
- propulsieafwijking.

### 6.3 Geofence
**Geofence**: virtuele grens waarbinnen het voertuig moet blijven.

### 6.4 Veilige degradatie
Bij storingen hoeft een drone niet altijd “door te vliegen”. Goede logica kiest een veilige terugvalmodus:
- terug naar handmatig;
- positiehold naar alt-hold;
- direct landen;
- RTL;
- disarm na landing.

---

## 7. Ontwikkel- en testketen

### 7.1 SIL
**Software-in-the-Loop (SIL)**: controller testen in simulatie zonder echte flight controllerhardware.

### 7.2 HIL
**Hardware-in-the-Loop (HIL)**: echte flight controller draait mee, maar de omgeving is nog gesimuleerd.

### 7.3 Bench test
**Bench test**: statische controle op de werkbank, liefst zonder propellers.

### 7.4 Indoor test
Gecontroleerde test met extra veiligheidsmaatregelen, lage energie en beperkte ruimte.

### 7.5 Flight test
Buitenproef of realistische binnentest onder operationele condities.

---

## 8. Prestatiebegrippen

### 8.1 Endurance
**Endurance**: vliegtijd onder een bepaalde belasting en vluchtconditie.

### 8.2 Payload
**Payload capacity**: extra massa die nog veilig kan worden meegenomen.

### 8.3 Throttle reserve
**Throttle reserve**: beschikbare vermogensmarge boven hover.

### 8.4 Vibration
**Trillingen**: mechanische verstoringen die sensoren en beeldkwaliteit verslechteren.

### 8.5 CG
**Center of Gravity (CG)**: massamiddelpunt. Een verkeerde CG maakt regelen moeilijker en inefficiënter.

---

## 9. Afkortingenlijst
| Afkorting | Betekenis |
|---|---|
| AC | Automatic Control |
| BEC | Battery Eliminator Circuit / spanningsregelvoorziening |
| CG | Center of Gravity |
| ESC | Electronic Speed Controller |
| EKF | Extended Kalman Filter |
| GCS | Ground Control Station |
| GNSS | Global Navigation Satellite System |
| GPS | Global Positioning System |
| HIL | Hardware-in-the-Loop |
| IMU | Inertial Measurement Unit |
| PID | Proportional-Integral-Derivative |
| PWM | Pulsbreedtemodulatie / stuursignaal |
| RC | Radio Control |
| RTL | Return to Launch |
| SAC | Semi-autonomous Control |
| SIL | Software-in-the-Loop |
| UAS/UAV | Unmanned Aircraft System / Vehicle |

---

## 10. Minimale taalregels voor een Teams-assistent
Gebruik bij definities steeds dit patroon:
1. **Eén-zinsdefinitie**
2. **Waarom het relevant is**
3. **Wat vaak misgaat in de praktijk**
4. **Verwijzing naar document 2, 3 of 4 als het om stappen, formats of FAQ gaat**

---

## Bronbasis
Gebaseerd op multicopter ontwerp-, simulatie-, HIL-, regel- en failsafe-materiaal uit de aangeleverde bronset, aangevuld met algemene drone-techniekkennis.
