# Reflektion - M3 v2

Mohammad Sami Alsharef

## Vad jag gjort
Jag byggde en "Mitt konto"-sida i ren HTML/CSS/JS som bygger pa samma
design som M1 + M2: G&S-meny, riktig logotyp, sage + oliv farger,
Georgia rubriker. Pa sidan kan man:

- Spara sitt namn (localStorage).
- Bygga en onskelista med riktiga produktkort fran kollektionen.
- Hamta vader for Stockholm och fa en jack-rekommendation (Fetch).
- Hamta ett slumpat visste-du (Fetch).
- Andra accentfargen pa hela sidan med en color-picker.
- Vaxla mellan ljust och morkt tema.

## Vad jag larde mig
- **CSS custom properties** - `--accent` + `setProperty()` gor det enkelt
  att andra accentfargen overallt utan att skriva om CSS-koden.
- **Fetch + Promise** - jag forstar nu .then/.catch-kedjan och varfor man
  ska hantera fel (om servern ar nere ska sidan inte krascha).
- **localStorage med JSON** - for att spara onskelistan kor jag
  `JSON.stringify()` nar jag sparar och `JSON.parse()` nar jag laddar.
- **ARIA & tangentbord** - `aria-live`, `aria-pressed`, `tabindex="0"` +
  keydown for Enter/Space/Delete. Det gor sidan anvandbar utan mus.
- **Custom focus-marker** - `outline: 3px dashed #ff7a00` syns mycket
  tydligare an webblasarens default.

## Vad som var svart
- Att fa Fetch-svaren att passa in i designen utan att andra layouten.
  Jag loste det med en liten `.vader-yta`-card med emoji + temp + tip.
- LocalStorage med JSON - jag hade fel forsta gangen for att jag
  glomde JSON.parse, sa jag fick en string istallet for ett array.

## Vad jag skulle gora harnast
- Lagga till en sokfunktion i onskelistan.
- Anvanda en API for valutakurser sa priserna kan visas i USD/EUR.
- Bygga en backend (Node.js?) sa flera enheter delar samma onskelista.
