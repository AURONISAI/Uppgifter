# Felanalys - Del 2

Sami

## index.html
1. Saknad doctype + lang -> quirks mode, skarmlasare vet inte sprak. Fix: la till.
2. Saknad charset + viewport -> svenska tecken brakar, mobil ser konstig ut. Fix: la till.
3. Title var "Felaktig Webbsida" -> dalig SEO. Fix: bytte till nat beskrivande.
4. `<img src="hav.webp">` -> ingen alt + filen fanns inte. Fix: alt + bild som finns.
5. Lank `<a href="#">Klicka har</a>` -> sager inget. Fix: tydliga lankar med riktiga mal.
6. Formular utan label och utan method -> tillganglighet + fel default GET. Fix: label+for/id, method=post.

## style.css
7. `lightgray` text pa `#eee` bakgrund -> nasten olasligt. Fix: svart pa vitt.
8. `font-size: 9px` -> for litet. Fix: 16px.
9. `lightblue` lankar pa ljus bakgrund -> dalig kontrast. Fix: oliv `#82a31a`.
10. Inga responsiva regler. Fix: `img max-width:100%` + `@media (max-width:600px)`.

## script.js
11. SyntaxError - saknad `}` -> hela scriptet kraschade. Fix: la till.
12. `var x = 10` utan semikolon. Fix: `const x = 10;`.
13. Funktionen anropades aldrig. Fix: `DOMContentLoaded`-anrop.
14. Funktionsnamn `test` sager inget. Fix: `visaTal`.
