# Samis studi giud

En komplett studieguide i Matematik 2 med fokus på **hur** och **varför**, så att du kan lösa uppgifter själv utan AI på prov.

---

## 1) Så pluggar du smart (min metod till dig)

Använd samma rutin på nästan alla matteproblem:

1. **Läs frågan 2 gånger**: vad frågas exakt?
2. **Markera givna värden**: siffror, punkter, formler.
3. **Välj metod**: lutning, substitution, pq-formel, statistikregel osv.
4. **Räkna steg för steg**: hoppa inte över mellanled.
5. **Kontrollera svaret**: sätt tillbaka i ursprungsekvationen eller rimlighetsbedöm.

Kort minnesregel: **Förstå -> Plan -> Lös -> Kontroll**.

---

## 2) Räta linjens ekvation (superviktigt)

### Grundform

`y = kx + m`

- `k` = lutning (hur brant linjen är)
- `m` = skärning med y-axeln (när `x = 0`)

### Hur du tänker

- Ser du `y = kx + m`? Läs av direkt:
  - lutning = talet framför `x`
  - y-skärning = konstanten

### Exempel (löst)

Uppgift: Vad är lutningen och y-skärningen för `y = -2x + 5`?

Lösning:
- Lutning `k = -2`
- Y-skärning `m = 5`

Varför: Formen är redan `y = kx + m`, alltså kan du läsa av direkt.

### Exempel (olöst - träna)

1. Bestäm `k` och `m` för `y = 4x - 7`.
2. Bestäm `k` och `m` för `y = -0,5x + 3`.

---

## 3) Parallella och vinkelräta linjer

### Regler

- **Parallella** linjer har **samma lutning**.
- **Vinkelräta** linjer har lutningar som uppfyller `k1 * k2 = -1`.
  - Praktiskt: ta negativa inversen.
  - Om `k = 2` blir vinkelrät lutning `-1/2 = -0,5`.

### Exempel (löst)

Uppgift: Vilken linje är vinkelrät mot `y = 2x - 3`?

Lösning:
- Originalets lutning är `2`
- Vinkelrät lutning = `-1/2 = -0,5`
- En korrekt linje är t.ex. `y = -0,5x + 4`

Varför: Endast negativa inversen ger 90 grader mellan linjerna.

### Exempel (olöst - träna)

1. Ge en linje som är parallell med `y = -3x + 1`.
2. Ge en linje som är vinkelrät mot `y = -3x + 1`.

---

## 4) Lutning mellan två punkter

Formel:

`k = (y2 - y1) / (x2 - x1)`

### Exempel (löst)

Punkter: `(2, 3)` och `(5, 9)`

`k = (9 - 3) / (5 - 2) = 6/3 = 2`

Varför: lutning = förändring i y per förändring i x.

### Vanliga misstag

- Byter ordning i täljare/nämnare olika -> fel tecken.
- Delar med fel x-differens.

### Exempel (olöst - träna)

1. Beräkna lutningen mellan `(1, -2)` och `(4, 7)`.
2. Beräkna lutningen mellan `(-3, 5)` och `(2, 5)`.

---

## 5) Ekvationssystem (två linjer)

Du har oftast två metoder:

### A) Substitution

Bra när en ekvation redan är löst för en variabel.

Steg:
1. Lös ut `y` eller `x` i en ekvation.
2. Sätt in i den andra.
3. Lös en variabel.
4. Sätt tillbaka för att få den andra.
5. Kontrollera i båda.

### B) Addition/elimination

Bra när koefficienter enkelt kan ta ut varandra.

Steg:
1. Justera ekvationerna så en variabel får motsatta koefficienter.
2. Addera/subtrahera ekvationerna.
3. Lös en variabel.
4. Sätt tillbaka och få den andra.

### Exempel (löst)

`y = 2x + 1`
`x + y = 7`

Sätt in `y` i andra:
`x + (2x + 1) = 7`
`3x + 1 = 7`
`3x = 6`
`x = 2`

`y = 2*2 + 1 = 5`

Svar: `(x, y) = (2, 5)`

Varför: skärningspunkten måste uppfylla båda ekvationerna samtidigt.

### Ingen lösning / en lösning / oändligt många

- **Ingen lösning**: parallella olika linjer (samma `k`, olika `m`)
- **En lösning**: linjerna skär varandra en gång
- **Oändligt många**: samma linje skriven på olika sätt

Exempel ingen lösning:
`y = 2x + 3` och `y = 2x - 4`

---

## 6) Algebra och prioriteringsregler

### Förenkla uttryck

Exempel (löst):

`3x - 2 + 4x + 5`
`= 7x + 3`

Varför: lika termer kan slås ihop (x med x, tal med tal).

### Prioriteringsordning

1. Parentes
2. Potens
3. Multiplikation/Division
4. Addition/Subtraktion

Exempel (löst):

`2 + 3*(4 - 1)`
`= 2 + 3*3`
`= 2 + 9`
`= 11`

---

## 7) Andragradsfunktioner (parabler)

Form:

`f(x) = ax^2 + bx + c`

### Viktig logik

- `a > 0` -> öppnar uppåt -> minimum
- `a < 0` -> öppnar nedåt -> maximum
- Symmetrilinje: `x = -b/(2a)`
- Extrempunkt: sätt in x-värdet i funktionen för att få y.

### Exempel (löst)

`f(x) = x^2 - 6x + 5`

`x_topp = -(-6)/(2*1) = 3`
`y_topp = f(3) = 9 - 18 + 5 = -4`

Extrempunkt: `(3, -4)`

---

## 8) Enkla kvadratiska ekvationer

Om du har:

`x^2 = N`

så blir:

`x = +-sqrt(N)`

Exempel (löst):
`x^2 = 64` -> `x = 8` eller `x = -8`

Varför: både positivt och negativt tal i kvadrat kan ge samma resultat.

---

## 9) Statistik: median, lådagram, normalfördelning

### Median

- Sortera först.
- Udda antal: mittersta.
- Jämnt antal: medel av de två i mitten.

### Lådagram

- Lådan visar mittersta 50% (Q1 till Q3).
- IQR = `Q3 - Q1`.

### Normalfördelning (68-95-99,7-regeln)

- `mu +- 1 sigma` -> ca 68%
- `mu +- 2 sigma` -> ca 95%
- `mu +- 3 sigma` -> ca 99,7%

Exempel (löst): `mu = 170`, `sigma = 5`

- 68% ligger i `[165, 175]`

---

## 10) Provstrategi utan AI (det du ska göra på nästa prov)

1. Skriv alltid upp given formel först.
2. Visa mellanled i varje steg.
3. Sätt en ruta runt slutsvaret.
4. Kontrollera tecken (`+/-`) och decimaler.
5. Om flera alternativ: räkna klart och jämför sist.

---

## 11) Vanliga fel och hur du undviker dem

- Glömmer minus vid vinkelrät lutning
  - Fix: skriv alltid "negativ invers" innan du räknar.
- Tar fel ordning i `(y2 - y1)/(x2 - x1)`
  - Fix: välj ordning en gång och håll samma i både täljare och nämnare.
- Hoppar över kontroll
  - Fix: sätt alltid in svaret i originalet.
- Blandar ihop parallell och vinkelrät
  - Fix: parallell = samma `k`, vinkelrät = `k1*k2 = -1`.

---

## 12) Träningsdel (för dig att lösa själv)

### A) Räta linjer

1. Bestäm lutning och y-skärning för `y = -3x + 8`.
2. Vilken linje är parallell med `y = 1,5x - 2`?
3. Ge en linje som är vinkelrät mot `y = -4x + 1`.

### B) Lutning mellan punkter

4. Beräkna lutningen mellan `(1, 2)` och `(5, 10)`.
5. Beräkna lutningen mellan `(-2, 4)` och `(3, -1)`.

### C) Ekvationssystem

6. Lös systemet:
   - `y = x + 3`
   - `2x + y = 12`

7. Vilket system har ingen lösning?
   - `y = 3x + 1` och `y = 3x - 5`
   - `y = -x + 2` och `y = x - 4`

### D) Andragrad/statistik

8. Hitta extrempunkten till `f(x) = x^2 - 4x + 1`.
9. Medianen av `3, 7, 8, 10, 11, 13, 14`?
10. Med `mu = 50`, `sigma = 4`: vilket intervall innehåller ca 95%?

---

## 13) Facit till träningsdelen (kolla efter att du försökt)

1. `k = -3`, `m = 8`
2. Alla med lutning `1,5` (t.ex. `y = 1,5x + 7`)
3. Vinkelrät lutning `1/4` (t.ex. `y = 0,25x - 6`)
4. `k = (10-2)/(5-1) = 8/4 = 2`
5. `k = (-1-4)/(3-(-2)) = -5/5 = -1`
6. `x = 3`, `y = 6`
7. Ingen lösning: `y = 3x + 1` och `y = 3x - 5`
8. Extrempunkt `(2, -3)`
9. `10`
10. 95%: `mu +- 2sigma = 50 +- 8` -> `[42, 58]`

---

## 14) Sista meddelandet från din lärare (viktigt)

Du behöver inte vara "snabbast". Du behöver vara **systematisk**.

Om du följer metoden i denna guide, visar mellanled och kontrollerar svar, kommer du kunna lösa uppgifterna själv på provet.

Du klarar det.