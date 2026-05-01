# Reflektion - M3

Mohammad Sami Alsharef

## Vad jag larde mig
- Hur Fetch API funkar med `.then()` kedjor och `.catch()` for fel.
- LocalStorage funkar bra for sma saker (namn, lista) men jag fick lara
  mig att alltid `JSON.stringify` / `JSON.parse` nar man sparar objekt.
- ARIA-attribut ar inte magi - de bara hjalper skarmlasare att forsta
  vad ett element ar (tex `aria-pressed` pa min tema-knapp).

## Hur jag forbattrade tillgangligheten
- Bytte ut "klicka har"-tankesatt mot tydliga rubriker per sektion.
- La till `aria-live="polite"` pa hellsningen och fakta-rutan sa
  skarmlasare laser nya texten utan att avbryta.
- Anpassad fokusmarkering med oranges streckad ram - syns
  tydligare an webblasarens default bla rektangel, sarskilt mot
  sage gron bakgrund.
- Tangentbordsnavigering pa rutorna i onskelistan (Enter/Delete
  tar bort - inte bara klick).
- Bilden har en beskrivande alt-text som forklarar att det ar en
  slumpbild (sa skarmlasare inte forsoker beskriva nat den inte vet).

## Plattform / interoperabilitet
- Testat i Chrome och Firefox - allt funkar likadant.
- Mobil-anpassning via `@media (max-width:600px)`: tema-knappen
  hoppar in i flodet och inputen tar full bredd.
- Inga browser-specifika prefix behovdes eftersom jag bara anvander
  standard CSS (flexbox, border-radius, transitions).

## Insikter
Tillganglighet ar inte nagot man "lagger pa" i slutet - det ar
nagot man borjar med. Semantiska taggar, label-for/id, alt-text
- om man gor ratt fran borjan blir det halften sa mycket jobb
sen att kora Lighthouse och fixa "rod" punkterna.
