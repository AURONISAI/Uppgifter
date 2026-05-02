# Inlamning M3 - Niva 3 (v2)

Mohammad Sami Alsharef

"Mitt konto"-sida for Samis Jackets. Bygger pa **samma design som M1+M2**:
riktig logotyp (`assets/logo.png`), riktiga produktbilder fran Unsplash,
sage `#c3cca6` + oliv `#82a31a`, Georgia rubriker och sticky G&S-meny.

## Filer
- `index.html` - semantisk HTML, ARIA, samma meny-struktur som M2.
- `style.css` - brand-stil, animerad rand, mobil-media-query, morkt lage,
  oranges streckad fokusmarkering.
- `script.js` - DOM, Fetch (x2), localStorage, accentfarg, toast.
- `assets/logo.png` - samma logga som anvandes i M2.

## Funktioner
1. **Hero** med riktig produktbild (Inci Coat fran Unsplash) + valkomst.
2. **Spara namn** - localStorage hellsning + toast-notis.
3. **Onskelista med riktiga produktkort** - klicka "+ Lagg till" -> en
   slumpad jacka ur kollektionen ritas med sin riktiga bild, namn och pris.
   Klick eller Enter/Delete tar bort. Allt sparas i localStorage.
4. **Vader-tips (Fetch nr 1)** - Stockholms vader fran open-meteo
   rekommenderar en jacka ur kollektionen utifran temperaturen.
5. **Visste-du (Fetch nr 2)** - kort fakta fran uselessfacts.
6. **Tema-farg** - `<input type="color">` byter accentfargen overallt
   live (CSS custom properties + `setProperty`). Sparas i localStorage.
7. **Morkt/ljust tema** - tema-knapp med `aria-pressed`, sparas.
8. **Toast-notiser** - `role="alert"` ruta nere i hornet vid varje atgard.

## Tillganglighet (niva 3)
- Semantiska taggar: header (hero), nav, main, section, footer, figure.
- ARIA: `aria-label`, `aria-live`, `aria-pressed`, `aria-labelledby`,
  `role="list"`, `role="listitem"`, `role="status"`, `role="alert"`,
  `aria-hidden` pa dekorativa element.
- Anpassad fokus: `outline: 3px dashed #ff7a00` med `outline-offset: 3px`.
- Tangentbordsnav: `tabindex="0"` pa korten + Enter/Space/Delete tar bort.
- Hog kontrast (svart pa vitt + WCAG-OK accent).
- Beskrivande alt-text pa alla bilder.

## Skillnad mot v1
v1 (`mohammad-sami/`) ar mer experimentell med 3D CSS-jacka och flip-kort.
v2 (`mohammad-sami-v2/`) anvander **samma riktiga design som M1+M2** med
logotyp och Unsplash-produktbilder - mer trogen mot brand-identiten.

Se `reflektion.md` for vad jag larde mig.
