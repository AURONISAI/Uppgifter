# Lärarbedömd uppgift 4 - Python

## Uppgift: Skapa ett digitalt bibliotekssystem

### Att lämna in
En `.py`-fil döpt till `lararbedomd-uppgift-4.py`. Databasfilen skapas
automatiskt så den ska inte skickas in.

### Beskrivning
Skapa ett enklare bibliotekssystem där användaren kan:
- Lägga till en ny bok (titel och författare).
- Söka efter böcker.
- Visa alla böcker.
- Lagra och läsa data från en SQLite-databas.
- Ha programmet uppdelat i minst två egna moduler.

### Syfte
- Fil- och databashantering
- Undantagshantering med try/except
- Uppdelning av koden i moduler och funktioner
- Kodstandard och struktur

### Tekniska krav
- Skapa en databasfil, t.ex. `bibliotek.db`, med tabell `bocker`
  (kolumner: `id`, `titel`, `forfattare`).
- Använd `sqlite3` för databasoperationer.
- Dela upp programmet i minst två moduler, t.ex. `databas.py` och `main.py`.
- Implementera en enkel meny i `main.py`.
- Använd `try/except` vid all fil- och databashantering.
- Koden ska vara läsbar, kommenterad och följa kodstandard.

### Exempel på användarflöde
```
1. Lägg till bok
2. Sök bok
3. Visa alla böcker
4. Avsluta
```

### Checklist inför inlämning
- [ ] Programmet kan köras utan fel
- [ ] Koden är uppdelad i minst två moduler
- [ ] Minst en funktion från varje modul används
- [ ] Undantagshantering vid databasanrop
- [ ] SQL används för att spara och läsa data
- [ ] Programmet är kommenterat och lätt att följa
- [ ] Testat att lägga till och visa flera böcker

### Inlämningsregler från läraren
- Skicka **endast** koden i en `.py`-fil
- Inte mapp, inte ZIP, inte RAR
- Koden SKA gå att köra direkt
- Klistra ALDRIG in koden i Omniway
