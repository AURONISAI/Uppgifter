# Inlamning M3 - Niva 3

Mohammad Sami Alsharef

Bygger vidare pa Samis Jackets-temat fran M1 och M2.
Sidan ar "Mitt konto" med fyra interaktiva sektioner.

## Filer
- `index.html` - semantisk HTML (header/nav/main/section/footer), ARIA-attribut.
- `style.css` - brand-farger, hog kontrast, oranges streckad fokusmarkering, mobil-media-query, morkt lage.
- `script.js` - DOM, Fetch, LocalStorage, tema-knapp.

## Funktioner
1. **Spara namn** - localStorage, hellsning visas direkt vid nasta besok.
2. **Onskelista** - klicka knappen for att lagga till slumpad jacka med slumpad farg. Sparas i localStorage. Klicka pa rutan (eller Enter/Delete) for att ta bort.
3. **Modetips** - hamtar fakta fran `uselessfacts.jsph.pl` (oppet API, CORS pa).
4. **Inspirationsbild** - slumpad bild fran picsum.photos.
5. **Bonus** - tema-knapp (ljust/morkt) sparad i localStorage med `aria-pressed`.

## Tillganglighet (niva 3)
- Semantiska taggar genomgaende.
- Minst 2 ARIA-attribut: `aria-label`, `aria-live="polite"`, `aria-pressed`, `role="status"`, `role="listitem"`.
- Anpassad fokusmarkering: `outline: 3px dashed #ff7a00`.
- Tangentbordsnavigering pa rutorna (`tabindex="0"` + Enter/Delete).
- Hog kontrast (svart pa vit, oliv `#82a31a` mot vitt = WCAG AA).
- `alt`-text pa bilden.

## Test
- Funkar i Chrome och Firefox.
- W3C-validerad HTML/CSS.
- Lighthouse: tillganglighet ~95+.
- Mobil testat i DevTools (under 600px).

Se `reflektion.md` for vad jag larde mig.
