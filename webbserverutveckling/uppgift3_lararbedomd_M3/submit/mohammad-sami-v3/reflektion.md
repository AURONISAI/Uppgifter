# Reflektion - M3 v3 (Katalog)

Mohammad Sami Alsharef

## Vad jag gjort
Jag byggde en riktig **produktkatalog** for Samis Jackets i ren
HTML/CSS/JS. Sex jacka-modeller med totalt 21 fargvarianter visas i ett
grid. Man kan filtrera pa farg, sortera pa pris/namn, oppna en modal
med detaljer + fargvaljare och spara favoriter i en onskelista.

Designen bygger pa samma brand som M1 + M2: G&S-meny med riktig
logotyp, sage `#c3cca6` + oliv `#82a31a` farger, Georgia rubriker.

## Vad jag larde mig
- **Datadriven UI** - allt bygger pa en `produkter`-array med
  `varianter`. Det gor att lagga till en ny jacka ar bara en
  rad data, inte ny HTML.
- **Modal/lightbox** - jag larde mig hur man bygger en tillganglig
  modal med `role="dialog"`, `aria-modal`, fokushantering och Esc-stang.
- **Filter + sort** - `Array.filter()` och `Array.sort()` med
  callback-funktioner. Jag forstar nu hur `localeCompare()` funkar
  for namn-sortering.
- **CSS Grid responsivt** - `repeat(auto-fill, minmax(220px, 1fr))`
  ger automatisk kolumn-anpassning utan media queries.
- **Bildoptimering** - `loading="lazy"` gor att katalog-bilderna laddas
  forst nar man scrollar dit.
- **Aspect-ratio med padding-top trick** - `padding-top:120%` tvingar
  alla produktbilder till samma format aven om kallbilderna varierar.

## Vad som var svart
- **Modalens fargvaljare** - jag ville att klick pa en fargcirkel
  skulle byta huvudbilden direkt utan att stanga modalen. Jag loste
  det med ett `valjVariant()`-funktion som uppdaterar `src` + `alt`.
- **Onskelistan med varianter** - att spara bade produkt-id och
  fargkod sa man ser exakt vilken farg man valt nar man laddar om.
- **Vader -> produkt** - att koppla temperatur till en specifik
  produkt ur katalogen och visa dess bild bredvid temperaturen.

## Vad jag skulle gora harnast
- Lagga till bilder i flera vinklar i modalen (carousel).
- Bygga en backend (Node.js?) sa onskelistan delas mellan enheter.
- Implementera en riktig kassa-flow med totalbelopp och leverans.
- Lagga till storleksvaljare (S/M/L/XL) i modalen.
