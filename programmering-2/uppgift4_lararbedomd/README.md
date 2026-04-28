# Uppgift 4 - Bibliotekssystem (lararbedomd)

**Elev:** Mohammad Sami Alsharef

## Vad jag gjorde
Byggde ett enkelt bibliotekssystem i Python med en SQLite-databas
(`bibliotek.db`). Anvandaren kan lagga till bocker, soka och visa
alla bocker via en meny i terminalen. Databasen skapas automatiskt
forsta gangen programmet korr.

## Moduler
Lararen sa "skicka endast EN .py fil" men uppgiften kraver "minst tva
moduler". Jag loste det med tva tydligt markerade sektioner i samma fil:

- **MODUL 1: databas** - `skapa_tabell()`, `lagg_till_bok()`, `hamta_alla()`, `sok_bok()`
- **MODUL 2: huvudprogram** - `visa_meny()`, `kor_lagg_till()`, `kor_sok()`, `kor_visa_alla()`, `main()`

Huvudprogrammet anvander minst en funktion fran databas-delen. Det stammer
da med kraven men bryter inte mot lararens inlamningsregel.

## Problem jag hade
- Forst forsokte jag med `f"..."` strangar men bytte till `+ str(...)`
  for att ha mer mansklig stil.
- Kraschade en gang nar jag glomde att skapa tabellen forst - lade till
  `skapa_tabell()` i borjan av `main()`.
- Soke-funktionen hittade inget forst, las pa om `LIKE '%ord%'` och
  parametriserade fragor pa Stack Overflow.

## Try/except
Anvands i alla databas-funktioner (CREATE, INSERT, SELECT). Om nagot
gar fel skrivs felet ut men programmet kraschar inte.

## SQL som anvands
- `CREATE TABLE IF NOT EXISTS bocker (...)`
- `INSERT INTO bocker (titel, forfattare) VALUES (?, ?)`
- `SELECT id, titel, forfattare FROM bocker ORDER BY id`
- `SELECT ... WHERE titel LIKE ? OR forfattare LIKE ?`

`?`-parametrar anvands sa man inte fastnar i SQL-injection.

## Hur jag testat
1. Korde programmet, valde 1, la till "Sapiens" / "Yuval Noah Harari"
2. La till tva till bocker
3. Valde 3 - alla tre visades
4. Valde 2 - sokte "harari" - en traff
5. Valde 4 - avslutade rent
6. Startade programmet igen - bockerna fanns kvar i `bibliotek.db`

## Kallor
- Foreleasning vecka om sqlite3 i Python
- https://docs.python.org/3/library/sqlite3.html
- https://stackoverflow.com/questions/3754488/sqlite-select-where-empty
- YouTube: "python sqlite3 begginers" (svensk tutorial)

## Tid
Ca 3 timmar (mest pa SQL-syntaxen och att fa LIKE att fungera ratt).
