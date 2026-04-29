# Felanalys - Del 2

Mohammad Sami Alsharef

Filerna jag laddade ner fran lararens GitHub hade flera problem.
Har gar jag igenom dem en och en, vad de orsakar och vad jag andrade.

## index.html

**1. Saknad doctype och sprak**
- Originalet borjade direkt med `<html>` utan `<!DOCTYPE html>` och utan `lang`.
- Pavorkan: webblasaren kan hamna i quirks mode och skarmlasare vet inte vilket sprak texten ar pa.
- Fix: la till `<!DOCTYPE html>` och `<html lang="sv">`.

**2. Saknad meta charset och viewport**
- Originalet hade ingen `<meta charset>` eller viewport.
- Pavorkan: svenska tecken (a, a, o) kan bli konstiga, och sidan blir oanvandbar pa mobil.
- Fix: la till `<meta charset="UTF-8">` och `<meta name="viewport" ...>`.

**3. Daligt title**
- "Felaktig Webbsida" sager inget om sidan.
- Pavorkan: dalig SEO och anvandaren ser bara skrap i flikens titel.
- Fix: bytte till en beskrivande titel.

**4. Bild utan alt och med fil som inte finns**
- `<img src="hav.webp">` - ingen alt-text, och hav.webp var inte med i mappen.
- Pavorkan: bilden visas inte, skarmlasare kan inte berattav vad det ar, brott mot tillganglighet.
- Fix: la till en `alt`-text och bytte till en bild som faktiskt finns (Unsplash-url).

**5. Vag lank**
- `<a href="#">Klicka har</a>` - texten "Klicka har" sager inget och hashtag-lanken leder ingenstans.
- Pavorkan: anvandaren vet inte vart lanken gar, och skarmlasare som lyssar igenom alla lankar pa en sida hor bara "klicka har, klicka har, klicka har".
- Fix: bytte till tydliga lankar med riktiga mal.

**6. Formular utan label och utan method**
- `<input type="text" name="namn">` saknade `<label>` och formen hade ingen `method`.
- Pavorkan: utan label kan en skarmlasare inte tala om vad input-faltet handlar om. Utan method skickas data som GET som default vilket inte alltid ar onskat.
- Fix: la till `<label for="namn">` kopplad till input-faltets `id`, samt `method="post"`.

## style.css

**7. Helt obeflig text**
- `color: lightgray` pa `background-color: #eee` - nastan samma farg, gick inte att lasa.
- Pavorkan: brott mot WCAG-kontrast, oanvandbart for personer med synnedsatning.
- Fix: morknade texten till `#222`.

**8. For liten text**
- `font-size: 9px` - alldeles for litet for att lasa bekvamt.
- Pavorkan: sidan blir trottsam att lasa, daligt for tillganglighet.
- Fix: andrade till 16px (standard).

**9. Lankar med dalig kontrast**
- `a { color: lightblue }` pa `#eee` bakgrund - syns knappt.
- Fix: morkare bla `#1f3a5f`.

**10. Ingen responsivitet**
- Inga regler for sma skarmar, inga `max-width` pa bilder.
- Fix: la till `img { max-width: 100% }` och en `@media`-query.

## script.js

**11. SYNTAX ERROR - saknad stangande }**
- Funktionen `function test() { ... ` hade ingen stangande klammerparentes.
- Pavorkan: hela scriptet kraschar - JavaScript-konsolen visar SyntaxError och inget i scriptet kors.
- Detta var det allvarligaste felet.
- Fix: la till `}` efter `console.log(x);`.

**12. Anvande var och saknade semikolon**
- `var x = 10` - var ar gammalt, modern JS anvander `let`/`const`. Saknat semikolon.
- Pavorkan: var har konstig scoping och kan ge svarspara buggar i storre projekt.
- Fix: bytte till `const x = 10;`.

**13. Funktionen anropades aldrig**
- `function test()` definierades men kallades aldrig.
- Pavorkan: aven om syntax-felet fixades skulle inget synas i konsolen.
- Fix: la till anrop i `DOMContentLoaded`.

**14. Meningslost namn**
- `test` sager inget om vad funktionen gor.
- Fix: dopte om till `visaTal`.
