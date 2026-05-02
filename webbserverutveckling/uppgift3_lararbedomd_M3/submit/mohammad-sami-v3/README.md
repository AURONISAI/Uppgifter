# Inlamning M3 - Niva 3 (v3 - Katalog)

Mohammad Sami Alsharef

En riktig **produktkatalog** for Samis Jackets. Bygger pa samma design
som M1 + M2 (G&S meny, sage + oliv farger, Georgia rubriker) men nu med
**vara riktiga produkter och riktiga produktfoton**.

## Produkter (6 modeller, 21 fargvarianter)
| Art.nr  | Namn          | Pris      | Fargvarianter |
|---------|---------------|-----------|---------------|
| 8805    | Storm Puffer  | 2 999 kr  | 3 |
| F-0357  | Edda Long     | 3 499 kr  | 3 |
| F-0445  | Inci Coat     | 2 499 kr  | 5 |
| F-0473  | Aurora Coat   | 2 799 kr  | 5 |
| F-0474  | Forest Bomber | 1 899 kr  | 3 |
| L01     | Nordic Light  | 1 599 kr  | 2 |

## Filer
- `index.html` - semantisk HTML, ARIA, samma meny-struktur som M2.
- `style.css` - brand-stil, animerad rand, mobil-media-query, morkt lage,
  oranges streckad fokusmarkering, modal/lightbox-stil.
- `script.js` - DOM, Fetch (x2), localStorage, modal, filter+sort.
- `assets/logo.png` - G&S logotyp.
- `assets/produkter/*.jpg` - 21 riktiga produktbilder.

## Funktioner
1. **Hero** med riktig produktbild (Aurora Coat).
2. **Katalog** med 6 produkter och 21 fargvarianter:
   - Filter pa farg (Beige, Svart, Brun, Khaki, Gron).
   - Sortering (standard / pris upp / pris ner / namn).
   - Live antal-info ("X av 6 modeller").
   - Fargcirklar pa varje kort visar tillgangliga varianter.
3. **Produktmodal (lightbox)** - klick pa produkt oppnar detalj-vy med:
   - Stor bild som byts nar man valjer farg.
   - Beskrivning, pris, fargvaljare (radiogroup ARIA).
   - "Lagg till i onskelistan"-knapp.
   - Esc, klick utanfor eller stang-knappen stanger.
4. **Onskelista** - sparas i localStorage med produkt-id + fargkod.
   Klick eller Enter/Delete tar bort. Live-raknare bade i sektionen och
   i menyn ("X i onskelistan").
5. **Vader-tips (Fetch nr 1)** - Stockholms vader fran open-meteo
   rekommenderar **en specifik produkt ur katalogen** med bild.
6. **Visste-du (Fetch nr 2)** - kort fakta fran uselessfacts.
7. **Tema-farg** - `<input type="color">` byter accentfargen overallt
   live (CSS custom properties). Sparas i localStorage.
8. **Morkt/ljust tema** - tema-knapp med `aria-pressed`.
9. **Toast-notiser** - `role="alert"` ruta nere i hornet.

## Tillganglighet (niva 3)
- Semantiska taggar: header, nav, main, section, footer.
- ARIA: `aria-label`, `aria-live`, `aria-pressed`, `aria-checked`,
  `aria-labelledby`, `aria-modal`, `aria-hidden`,
  `role="list"`, `role="listitem"`, `role="status"`, `role="alert"`,
  `role="dialog"`, `role="radiogroup"`, `role="radio"`.
- Anpassad fokus: `outline: 3px dashed #ff7a00`.
- Tangentbordsnav: `tabindex="0"` pa kort, Enter/Space oppnar modal,
  Esc stanger den, Delete tar bort fran onskelistan.
- Beskrivande alt-text pa alla bilder (innehaller produktnamn + farg).
- `loading="lazy"` pa katalogbilderna for prestanda.

## Skillnad mot tidigare versioner
- **v1** (`mohammad-sami/`) - experimentell med 3D CSS-jacka.
- **v2** (`mohammad-sami-v2/`) - Unsplash-bilder.
- **v3** (`mohammad-sami-v3/`) - **riktig produktkatalog med riktiga
  produktfoton fran var kollektion**. Den mest "shop-mojliga" versionen.

Se `reflektion.md` for vad jag larde mig.
