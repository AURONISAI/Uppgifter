# Förberedelse inför Bedömningsmöte - Matematik 2
### Mohammad Sami Alsharef

*Läs igenom detta NOGA dagen innan. Det är allt vi gått igenom.*
*Under BM: papper, penna, miniräknare och formelblad. Inget annat.*

---

## Snabb påminnelse - Vad kan dyka upp?

Allt från modul 1 till 11 kan komma. Tänk på att frågor kan likna
lärarbedömda uppgifter men med ANDRA tal. Lär dig metoden, inte svaret.

---

## 1. Statistik och Normalfördelning

### Medelvärde, median, typvärde

**Medelvärde** = summan av alla tal delat med hur många tal det är
```
tal: 4, 7, 9, 2, 8
summa = 30
antal = 5
medelvärde = 30 / 5 = 6
```

**Median** = mittersta värdet (sortera FÖRST!)
```
sortera: 2, 4, 7, 8, 9
mittersta = 7   (plats 3 av 5)

om jämnt antal:
2, 4, 7, 8 → (4 + 7) / 2 = 5,5
```

**Typvärde** = det tal som förekommer flest gånger
```
2, 3, 3, 5, 7, 3 → typvärde = 3
```

### Normalfördelning - Det VIKTIGASTE

Normalfördelningskurvan är klockformad och symmetrisk.

**68-95-99,7 regeln:**
```
μ ± 1σ  →  68%  av alla värden
μ ± 2σ  →  95%  av alla värden
μ ± 3σ  →  99,7% av alla värden
```

Hur man tänker: räkna hur många σ bort från μ intervallet är.

*Exempel:*
Klassen har μ = 170 cm, σ = 5 cm
Fråga: hur stor andel är mellan 165 och 175?

165 = 170 − 5 = μ − 1σ
175 = 170 + 5 = μ + 1σ
→ ±1σ → **68%**

**Att läsa av från en graf:**
Toppen på kurvan = medelvärdet (μ).
Kurvan är alltid symmetrisk runt toppen.

**Standardavvikelse (σ):**
Berättar hur utspridd datan är.
- Liten σ = datan klumpar sig nära medelvärdet
- Stor σ = datan är spridd

### Lådagram (box plot)

```
    Min ---[Q1 --- Median --- Q3]--- Max
              |      LÅDAN      |
              |    50% av data  |
```

- Q1 = 25% av datan är under detta
- Median = 50% av datan är under detta  
- Q3 = 75% av datan är under detta
- Lådan visar mittersta 50% (från Q1 till Q3)
- IQR = Q3 − Q1 (lådans bredd)

Typfråga: *"Vad visar lådan?"* → mittersta 50% av värdena

---

## 2. Algebra - Förenkla och Räkna

### Lika termer

Man kan bara addera/subtrahera termer av SAMMA typ.

```
3x + 5x = 8x        ✓ (båda är x)
3x + 5 = 3x + 5     ✓ (kan inte förenklas mer)
3x + 5x + 2 − x = 7x + 2
```

### Multiplicera parenteser

```
3(x + 4) = 3x + 12
−2(x − 5) = −2x + 10   ← minustecknet byter tecken på allt inne
```

### Kvadreringsregler (VIKTIGA!)

```
(a + b)² = a² + 2ab + b²
(a − b)² = a² − 2ab + b²
```

*Exempel:*
```
(x + 3)² = x² + 6x + 9
(x − 4)² = x² − 8x + 16
```

Vanligt misstag: (x + 3)² ≠ x² + 9. Man glömmer mittentermen!

### Konjugatregeln

```
(a + b)(a − b) = a² − b²
```

*Exempel:*
```
(x + 5)(x − 5) = x² − 25
(3 + y)(3 − y) = 9 − y²
```

### Potensregler

```
a⁰ = 1           (vad som helst upphöjt till 0 = 1)
a¹ = a
aᵐ · aⁿ = aᵐ⁺ⁿ  (multiplicera → addera exponenter)
aᵐ / aⁿ = aᵐ⁻ⁿ  (dividera → subtrahera exponenter)
(aᵐ)ⁿ = aᵐ·ⁿ   (potens av potens → multiplicera)
a⁻ⁿ = 1/aⁿ      (negativ exponent → bråk)
```

*Exempel:*
```
x³ · x² = x⁵
x⁶ / x² = x⁴
(x²)³ = x⁶
x⁻² = 1/x²
```

Prioriteringsordning (kom ihåg PPPP):
1. Parenteser
2. Potenser
3. Punkträkning (· och /)
4. Plusminus (+ och −)

---

## 3. Ekvationer

### Linjär ekvation - En obekant

Målet: få x ensamt på ena sidan.

Gör SAMMA sak på båda sidor hela tiden.

```
5x − 7 = 8
5x = 8 + 7
5x = 15
x = 15 / 5
x = 3
```

Kontrollera alltid: sätt in x i originaluttrycket → ska bli sant.

### Enkla andragrads - x² = tal

```
x² = 64
x = ±√64
x = 8  eller  x = −8
```

ALLTID två svar! Minus-svaret glöms ofta bort.

### Andragrads - ax² + bx + c = 0

Använd PQ-formeln eller kvadratkompletering.

**PQ-formeln** (när a = 1):
Om x² + px + q = 0:
```
x = −p/2 ± √((p/2)² − q)
```

**Den allmänna formeln** (alla a):
```
x = (−b ± √(b² − 4ac)) / (2a)
```

*Exempel - hitta nollställen till f(x) = x² − 6x + 5:*
```
a=1, b=−6, c=5
x = (6 ± √(36 − 20)) / 2
x = (6 ± √16) / 2
x = (6 ± 4) / 2

x₁ = (6 + 4) / 2 = 5
x₂ = (6 − 4) / 2 = 1
```

Kontroll: f(1) = 1 − 6 + 5 = 0 ✓ och f(5) = 25 − 30 + 5 = 0 ✓

### Ekvationssystem - Två obekanta

**Substitutionsmetoden:**
```
y = 2x + 1    ... (1)
y = x + 4     ... (2)

Sätt (1) i (2):
2x + 1 = x + 4
x = 3

y = 2(3) + 1 = 7

Svar: x = 3, y = 7
```

**Additionsmetoden:**
```
2x + y = 8    ... (1)
x − y = 1     ... (2)

Addera (1) + (2):
3x = 9
x = 3

Sätt in i (2): 3 − y = 1 → y = 2

Svar: x = 3, y = 2
```

---

## 4. Funktioner

### Linjär funktion - Räta linjen

```
y = kx + m
```

- **k** = lutning (hur brant linjen är)
  - k > 0 → linjen stiger åt höger
  - k < 0 → linjen sjunker åt höger
  - k = 0 → horisontell linje

- **m** = y-axelns skärningspunkt (där linjen korsar y-axeln)

*Exempel: y = 2x + 3*
När x = 0: y = 3 (skär y-axeln vid y = 3)
Lutning = 2 (för varje steg höger, gå 2 steg upp)

**Hitta lutningen från två punkter:**
```
k = (y₂ − y₁) / (x₂ − x₁)
```

**Parallella linjer** har samma k-värde.

### Andragradsfunktion - Parabeln

```
f(x) = ax² + bx + c
```

Det här är det viktigaste i modul 2!

**Symmetrilinje:**
```
x = −b / (2a)
```

Det är också x-koordinaten för extrempunkten (vertex).

**Extrempunkt:**
1. Räkna x med formeln ovan
2. Sätt in x i f(x) → får y
3. Extrempunkt = (x, y)

**Öppnar kurvan uppåt eller nedåt?**
- a > 0 → uppåt (som ett U) → minimum
- a < 0 → nedåt (som ett ∩) → maximum

**Nollställen** (var parabeln korsar x-axeln):
Lös f(x) = 0 med andragradformeln.

*Fullständigt exempel:*
```
f(x) = x² − 6x + 5

a = 1, b = −6, c = 5

Symmetrilinje: x = −(−6)/(2·1) = 6/2 = 3

Extrempunkt:
f(3) = 9 − 18 + 5 = −4
Point: (3, −4)  → minimum (a > 0)

Nollställen: x² − 6x + 5 = 0
x = (6 ± √(36−20))/2 = (6 ± 4)/2
x = 5 eller x = 1
```

**Tillämpning med rörelse:**

Om höjd/avstånd beskrivs med h(t) = at² + bt + c:
- Maximal höjd → hitta maximum (samma formel)
- t = starttid, h(0) = c = starthöjden

---

## 5. Derivata (grundläggande)

Derivatan beskriver hur snabbt en funktion förändras = lutningen i en punkt.

**Notation:** f'(x) läses "f prim av x"

**Derivationsregler:**
```
f(x) = c     →  f'(x) = 0         (konstant → derivata noll)
f(x) = x     →  f'(x) = 1
f(x) = xⁿ   →  f'(x) = n·xⁿ⁻¹   (viktigaste regeln!)
f(x) = kx   →  f'(x) = k
```

*Exempel:*
```
f(x) = x³   →  f'(x) = 3x²
f(x) = x²   →  f'(x) = 2x
f(x) = 5x   →  f'(x) = 5
f(x) = 7    →  f'(x) = 0
```

**Vad derivatan berättar:**
```
f'(x) > 0  →  funktionen är VÄXANDE (stiger) i det intervallet
f'(x) < 0  →  funktionen är AVTAGANDE (sjunker) i det intervallet
f'(x) = 0  →  extrempunkt (lokal max eller min)
```

**Hitta extrempunkt med derivata:**
1. Derivera: räkna ut f'(x)
2. Lös f'(x) = 0 → ger x-värdet
3. Sätt in x i f(x) → ger y-värdet
4. Extrempunkt = (x, y)

*Exempel:*
```
f(x) = x² − 6x + 5
f'(x) = 2x − 6

Extrempunkt: 2x − 6 = 0 → x = 3
f(3) = 9 − 18 + 5 = −4
Extrempunkt: (3, −4)
```

Samma svar som med symmetrilinjen! Båda metoderna fungerar.

---

## 6. Exponentialfunktioner

```
f(x) = a · bˣ
```

- **a** = startvärde (när x = 0)
- **b** = bas (förändringsfaktorn)
  - b > 1 → exponentiell TILLVÄXT (ökar)
  - 0 < b < 1 → exponentiellt FÖRFALL (minskar)

*Exempel:*
```
f(x) = 100 · 1,05ˣ  → 5% ökning per steg
f(x) = 500 · 0,9ˣ   → 10% minskning per steg
```

**Förändringsfaktor:**
- Ökar med 15% → multiplicera med 1,15
- Minskar med 20% → multiplicera med 0,80

---

## Inför BM - Tänk på detta

**Du får ha med:**
- Papper och penna (ta med tillräckligt)
- Miniräknare
- Formelblad (SKRIVET UT på papper - ladda ner från Omniway)
- Giltig legitimation (VIKTIGT, annars får du inte göra mötet)

**Du får INTE använda:**
- Lärobok
- Gamla uträkningar (inga anteckningar)
- Mobil för att slå upp saker

**Kameran måste vara PÅ hela mötet.**

---

## Vanliga Frågetyper - Öva på dessa

1. Läs av ett lådagram - vad är Q1, Q3, IQR?
2. Normalfördelning - hur stor andel ligger inom ett intervall?
3. Räkna ut medelvärde och median från en lista med tal
4. Förenkla algebrauttryck (multiplicera parenteser, lika termer)
5. Lösa en ekvation steg för steg
6. Hitta symmetrilinje + extrempunkt för f(x) = ax² + bx + c
7. Tolka en andragradsfunktion i ett verkligt sammanhang (raket, boll, etc.)
8. Räkna med potensregler
9. Hitta lutning (k) och skärningspunkt (m) för en rät linje
10. Derivera en enkel funktion

---

*Lycka till på bedömningsmötet!*
*Visa hur du tänker - det är lika viktigt som rätt svar.*
