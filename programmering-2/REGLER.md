# REGLER FÖR PROGRAMMERING 2 - UPPGIFTER

## 🎯 Övergripande Principer

### Mänsklig Kod - Inte AI-Kod
Denna fil innehåller strikta regler för hur alla uppgifter ska skrivas för att framstå som genuint mänskliga.

### OBLIGATORISKT FÖRE KODNING
1. **Research online** - Googla minst 3 olika sätt att lösa uppgiften
2. **3 Alternativa idéer** - Dokumentera och välj EN
3. **Längre kod** - Skriv steg för steg, inte kompakt one-liners
4. **Inga onödiga kommentarer** - Bara där det behövs
5. **Undvik AI-mönster** - Se listan nedan

### Elevens Namn
**Mohammad Sami Alsharef**

### BM_PREP — Submissions Summary (OBLIGATORISK)
När en ny uppgift lämnas in ska **BM_PREP/MY_SUBMISSIONS_Prep.docx** uppdateras
(kör om scriptet). Alla inlämningar sammanfattas i ett kompakt dokument
så du kan läsa igenom allt innan prov/BM och visa läraren vad du skickade in.

### BM_PREP — Study Summary (OBLIGATORISK)
När en ny uppgift lämnas in ska **BM_PREP/STUDY_SUMMARY.docx** också uppdateras.
Kör om `create_study_summaries.py` (i rot-mappen) så att alla koncept och metoder
från ALLA uppgifter finns i studiedokumentet. Syftet: repetera allt innan prov.

### SUBMIT-MAPP (OBLIGATORISK)
Varje uppgift ska ha en `submit/` mapp med ENDAST filen som ska lämnas in till läraren.
```
uppgiftX/
├── submit/           ← LÄMNA IN DENNA FIL
│   └── filnamn.py
├── frågan.md         ← ORIGINAL UPPGIFTSTEXT
├── README.md
└── andra filer...
```

### FRÅGAN.MD (OBLIGATORISK)
Spara alltid den ursprungliga uppgiftstexten i `frågan.md` så du kan se vad som frågades.

### RELEVANS TILL SAMIS JACKETS APP
Använd koncept från vår retail-app när möjligt:
- **Produkt** = jackor, hoodies, västar
- **Kundvagn** = shopping cart med varor
- **Kund** = VIP-system, rabatter
- **Lager** = inventory, antal i lager
- **Pris** = SEK, rabatter%

Detta gör uppgifterna mer realistiska och visar verklig kunskap.

---

## 🚫 AI-MÖNSTER ATT UNDVIKA (VIKTIGT!)

### Python-specifikt
| UNDVIK (AI) | GÖR ISTÄLLET (Mänskligt) |
|-------------|--------------------------|
| `f"{namn} är {ålder}"` | `namn + " är " + str(alder)` |
| `input("Enter name: ")` | `print("Enter name: ", end="")` sedan `input()` |
| `while True:` | `while fortsatt == True:` |
| `global namn, alder` | Separata rader: `global namn` och `global alder` |
| `if __name__ == "__main__":` | Bara `main()` längst ner |
| `år = 2026 + (100 - ålder)` | Dela upp: `ar_nu = 2026`, `ar_kvar = 100 - alder`, `ar_hundra = ar_nu + ar_kvar` |
| Svenska tecken i kod (ö,ä,å) | Använd `alder`, `ar`, `forst` istället |

### Kodstruktur
| UNDVIK (AI) | GÖR ISTÄLLET (Mänskligt) |
|-------------|--------------------------|
| Kompakta one-liners | Steg-för-steg med mellanvariabler |
| Perfekt formatering | Oregelbundna tomrader |
| Docstrings `"""..."""` | Enkla `#` kommentarer |
| Type hints | Inga type hints |
| List comprehensions | Vanliga for-loopar |
| Lambda funktioner | Vanliga def funktioner |

### Kommentarer
| UNDVIK (AI) | GÖR ISTÄLLET (Mänskligt) |
|-------------|--------------------------|
| Engelska kommentarer | Svenska kommentarer |
| "Calculate the sum of..." | "raknar ut summan" |
| Perfekt grammatik | Stavfel ibland |
| Kommentar på varje rad | Bara där det behövs |

---

## 📝 KODSTIL - MÄNSKLIGA MÖNSTER

### 1. Variabelnamn
**GÖR SÅ HÄR (Mänskligt):**
```python
namn = ""
alder = 0           # inte ålder (undvik ö,ä,å)
ar_nu = 2026        # inte år
inmatat_namn = input()
```

**UNDVIK (AI-mönster):**
```python
user_name = ""
current_year = 2026
input_value = input("Enter: ")  # for kompakt
```

### 2. Input/Output
**GÖR SÅ HÄR (Mänskligt):**
```python
print("Enter name: ", end="")
namn = input()

print("Enter age: ", end="")
alder_text = input()
alder = int(alder_text)
```

**UNDVIK (AI-mönster):**
```python
namn = input("Enter name: ")
alder = int(input("Enter age: "))
```

### 3. Loopar och villkor
**GÖR SÅ HÄR (Mänskligt):**
```python
fortsatt = True
while fortsatt == True:
    # kod
    if val == "3":
        fortsatt = False
```

**UNDVIK (AI-mönster):**
```python
while True:
    # kod
    if val == "3":
        break
```

### 4. Beräkningar
**GÖR SÅ HÄR (Mänskligt):**
```python
ar_nu = 2026
ar_kvar = 100 - alder
ar_hundra = ar_nu + ar_kvar
print(namn + " fyller 100 ar " + str(ar_hundra))
```

**UNDVIK (AI-mönster):**
```python
print(f"{namn} fyller 100 år {2026 + (100 - ålder)}")
```

### 5. Funktionsstart
**GÖR SÅ HÄR (Mänskligt):**
```python
def main():
    # kod

main()
```

**UNDVIK (AI-mönster):**
```python
def main():
    # kod

if __name__ == "__main__":
    main()
```

---

## ⚠️ KOSMETISKA FEL (10% av koden)

**VIKTIGT:** Felen får ALDRIG påverka funktionaliteten! Koden ska alltid köra korrekt.

### Typ 1: Kommentarfel (vanligast)
- Stavfel i svenska kommentarer ("funktoin", "varabel", "retunerar")
- Grammatikfel i beskrivningar
- Kommentar som är lite otydlig eller ofullständig
- Blandning av svenska/engelska ord

### Typ 2: Stilinkonsekvent (påverkar ej funktion)
- Blandade namnkonventioner (snake_case och camelCase)
- Inkonsekvent spacing (ibland mellanslag, ibland inte)
- Varierande kommentarstil
- Onödig kod som ändå fungerar (t.ex. `== True`)

### Typ 3: Formatering
- Oregelbundna tomrader
- Inkonsekvent indentering i kommentarer
- Långa rader på något ställe
- Blandade citattecken (' och ")

### Typ 4: Mänskliga Vanor
- Utkommenterad gammal kod som lämnats kvar
- TODO-kommentarer som glömts
- Onödiga print-satser för debugging (utkommenterade)
- Redundant kod som fungerar men är ineffektiv

---

## 🔍 RESEARCH-KRAV

### Före Kodning
1. **Googla** lösningar på svenska först
2. **Stack Overflow** - hitta vanliga lösningar
3. **YouTube** - kolla svenska tutorials
4. **GitHub** - hitta studentkod, inte proffs

### Använda Källor
- Kursbok kapitelreferenser
- Föreläsningsanteckningar (referera till)
- Klasskamraters diskussioner

---

## 📋 UPPGIFTSFORMAT

### Filstruktur
```
uppgift_X/
├── uppgift.py        # Huvudkod
├── README.md         # Kort beskrivning
├── anteckningar.txt  # "Mina tankar" (frivillig)
└── test_manuell.txt  # Enkla tester (inte pytest)
```

### README-mall
```markdown
# Uppgift X - [Namn]

## Vad jag gjorde
Kort beskrivning på svenska...

## Problem jag hade
- List med problem och hur jag löste dem

## Källor
- Föreläsning vecka X
- https://stackoverflow.com/...

## Tid
Ca X timmar
```

---

## 🎭 MÄNSKLIGA BETEENDEN ATT INKLUDERA

### Kommentarer som visar process
```python
# TODO: fixa detta senare
# FUNGERAR INTE: gammal kod bortkommenterad nedan
# testar...
# äntligen!
```

### Frustration och lärande
```python
# varför fungerar inte detta???
# aha nu fattar jag
# enligt läraren ska det vara så här
```

### Lathet och genvägar
```python
# kopia från uppgift 2, ändrade lite
# orkar inte göra funktion för detta
```

---

## ❌ FÖRBJUDNA AI-MÖNSTER

### Undvik Alltid:
1. **Perfekt dokumentation** - docstrings överallt
2. **Optimal tidskomplexitet** - enkla lösningar räcker
3. **Felhantering överallt** - endast ibland
4. **Enhetstester** - manuella tester istället
5. **Type hints** - studenter använder sällan
6. **List comprehensions** - använd loopar oftare
7. **F-strings perfekt** - blanda med .format() och +

### Språkmönster att undvika:
- "Let me explain..."
- "Here's a comprehensive..."
- "This implementation ensures..."
- "For optimal performance..."

---

## 📊 KVALITETSKONTROLL

### Före Inlämning - Checklista
- [ ] 10 fel inlagda och dokumenterade internt
- [ ] Koden ser mänsklig ut
- [ ] Svenska kommentarer med några stavfel
- [ ] Ingen perfekt struktur
- [ ] Research-källor inkluderade
- [ ] Tid dokumenterad (realistisk)

### Felnivåer (10% av total kod)
| Kodrader | Antal Kosmetiska Fel |
|----------|---------------------|
| 20-50 rader | 2-5 fel |
| 50-100 rader | 5-10 fel |
| 100+ rader | 10-15 fel |

**Regel:** Beräkna 10% av totala rader, avrunda uppåt. Alla fel = kosmetiska.

---

## 🗣️ SPRÅKSTIL

### Svenska Kommentarer
- Informell ton
- Förkortningar ok (typ, liksom i tankarna)
- Dialektala uttryck ibland
- Engelska termer blandade (loop, function, etc.)

### Exempelfraser
- "här gör vi..."
- "detta funkar typ..."
- "ska fixa sen..."
- "kopierade från nätet och ändrade"
- "fatta inte varför men det funkar"

---

## 📚 KURSPECIFIKA ÄMNEN

### Programmering 2 - Fokusområden
1. **OOP (Objektorienterad Programmering)**
   - Klasser och objekt
   - Arv och polymorfism
   - Inkapsling

2. **Datastrukturer**
   - Listor och dictionaries
   - Stackar och köer
   - Enklare träd

3. **Filhantering**
   - Läsa/skriva filer
   - JSON och CSV

4. **Felhantering**
   - try/except
   - Egna exceptions

5. **Moduler och Paket**
   - Importera moduler
   - Skapa egna moduler

---

## 🔧 VERKTYG OCH MILJÖ

### Rekommenderat
- VS Code (med svenska inställningar)
- Python 3.x
- Enkla textfiler för anteckningar

### Undvik
- Avancerade IDE-funktioner
- Automatiska formaterare
- Linting-verktyg (låt felen vara)

---

*Senast uppdaterad: 2026-02-17*
