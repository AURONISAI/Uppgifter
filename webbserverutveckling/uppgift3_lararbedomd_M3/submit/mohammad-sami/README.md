# Inlamning M3 - Niva 3

Mohammad Sami Alsharef

"Mitt konto"-sida for Samis Jackets - bygger vidare pa M1+M2.

## Filer
- `index.html` - semantisk HTML, hero med 3D-jacka, 6 sektioner, ARIA.
- `style.css` - brand-stil, CSS 3D (perspective + rotateX/Y), morkt lage,
  oranges streckad fokusmarkering, mobil-media-query, animerad gradient.
- `script.js` - DOM, Fetch (x2), localStorage, parallax, toast.

## Funktioner
1. **Hero med 3D-jacka** - byggd med rena CSS-lager (`perspective`,
   `transform-style: preserve-3d`, `rotateX/Y`, `translateZ`). Sjalv-svajar
   och foljer musrorelser (parallax via JS).
2. **Spara namn** - localStorage hellsning vid aterbesok + toast-notis.
3. **Onskelista med 3D flip-kort** - klicka "+ Lagg till" -> slumpad jacka
   ritas. Hovra/fokusera kortet -> det vrider sig 180° och visar pris.
   Klick eller Enter/Delete tar bort. Allt sparas i localStorage.
   Raknare uppdateras live.
4. **Vader-tips (Fetch nr 1)** - hamtar Stockholms vader fran open-meteo
   och rekommenderar en jacka utifran temperaturen.
5. **Visste-du (Fetch nr 2)** - kort fakta fran uselessfacts API.
6. **Tema-farg** - `<input type="color">` byter accentfargen overallt
   live (CSS custom properties + `setProperty`). Sparas i localStorage.
7. **Inspirationsbild** - slumpad fran picsum.photos.
8. **Morkt/ljust tema** - tema-knapp med `aria-pressed`, sparas.
9. **Toast-notiser** - `role="alert"` ruta nere i hornet.

## Tillganglighet (niva 3)
- Semantiska taggar: header (i hero), nav, main, section, footer.
- ARIA: `aria-label`, `aria-live`, `aria-pressed`, `aria-labelledby`,
  `role="list"`, `role="listitem"`, `role="status"`, `role="alert"`,
  `aria-hidden` pa det dekorativa 3D-elementet.
- Anpassad fokus: `outline: 3px dashed #ff7a00` med `outline-offset: 3px`.
- Tangentbordsnav: `tabindex="0"` pa flip-korten + Enter/Space/Delete.
- Hog kontrast (svart pa vitt + WCAG-OK accent).
- Beskrivande alt-text pa bilden, formular har label-for/id koppling.

## Test
- Funkar i Chrome, Firefox och Edge.
- W3C-validerad HTML/CSS.
- Lighthouse tillganglighet ~95+.
- Mobil testat under 600px (3D-jackan skalar ner, hero blir vertikal).

Se `reflektion.md` for vad jag larde mig.
