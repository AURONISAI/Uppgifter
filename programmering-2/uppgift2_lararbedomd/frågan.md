# Lärarbedömd uppgift 2 – Python

**Titel:** Hantera användardata i ett enklare system

## Att lämna in
En .py fil döpt till `lararbedomd-uppgift-2.py`

## Vad du ska visa i den här uppgiften
Den här uppgiften bygger på det du har lärt dig i Modul 2. Du ska visa att du kan:
- Planera program med algoritmtänk.
- Använda listor, dictionaries och tuples.
- Skriva funktioner för att strukturera din kod.
- Använda loopar, villkor och användarinmatning.
- Använda sökning och sortering i listor.
- Strukturera din kod så att den är läsbar och lätt att följa.

## Uppgift
Skapa ett program där användaren kan hantera en lista med användare. Programmet ska ge användaren möjlighet att:
1. Lägga till användare med namn, ålder och e-post.
2. Söka efter användare via namn eller e-post.
3. Visa alla användare sorterade alfabetiskt efter namn.
4. Avsluta programmet.

Du ska använda funktioner för att dela upp din kod. Ditt program ska vara användarvänligt, tydligt kommenterat och skrivet med god struktur.

## Bedömning – det här tittar läraren på
- Användning av listor och dictionaries.
- Att programmet är uppdelat i funktioner med tydligt syfte.
- Att menyn fungerar och att programmet är logiskt uppbyggt.
- Att du använder villkor, loopar och inmatning korrekt.
- Att du visar förståelse för sortering, sökning och datastrukturer.
- Att din kod är läsbar och kommenterad.

## Checklista före inlämning
- [ ] Jag har en fungerande meny med val 1–4.
- [ ] Jag använder en lista med dictionaries för att lagra användare.
- [ ] Jag har skapat och använt minst tre egna funktioner.
- [ ] Jag har testat mitt program – alla val fungerar.
- [ ] Jag har kommenterat min kod där det behövs.

## Mallkod att utgå ifrån
```python
# Funktion: Lägg till en användare
def add_user(users):
    # Här ska du skriva kod för att läsa in namn, ålder och e-post
    # Skapa en dictionary med informationen och lägg till i listan 'users'
    pass

# Funktion: Sök efter en användare
def search_user(users):
    # Be användaren skriva in ett sökord (t.ex. namn eller e-post)
    # Sök i listan efter matchande användare och skriv ut resultat
    pass

# Funktion: Visa alla användare
def show_users(users):
    # Sortera användarna efter namn
    # Skriv ut all information om varje användare
    pass

# Huvudfunktion: Sköter meny och programflöde
def main():
    users = []  # Här lagras användarna som dictionaries
    while True:
        print("\n1. Lägg till användare\n2. Sök användare\n3. Visa alla användare\n4. Avsluta")
        choice = input("Välj ett alternativ: ")
        if choice == "1":
            add_user(users)
        elif choice == "2":
            search_user(users)
        elif choice == "3":
            show_users(users)
        elif choice == "4":
            print("Programmet avslutas.")
            break
        else:
            print("Ogiltigt val, försök igen.")

# Starta programmet
main()
```
