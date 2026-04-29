# Mohammad Sami Alsharef
# bibliotekssystem lararbedomd 4
# main-modul: meny och anvandarinmatning
# databas-funktionerna ligger i en egen fil (databas.py)

import databas


def visa_meny():
    print("")
    print("=== Bibliotekssystem ===")
    print("1. Lagg till bok")
    print("2. Sok bok")
    print("3. Visa alla bocker")
    print("4. Avsluta")
    print("Val: ", end="")
    val = input()
    return val


def kor_lagg_till():
    print("Titel: ", end="")
    titel = input()

    print("Forfattare: ", end="")
    forfattare = input()

    if titel == "" or forfattare == "":
        print("Du maste skriva bade titel och forfattare.")
        return

    ok = databas.lagg_till_bok(titel, forfattare)
    if ok == True:
        print("Boken '" + titel + "' tillagd!")
    else:
        print("Nagot gick fel, boken sparades inte.")


def kor_sok():
    print("Sok efter (titel eller forfattare): ", end="")
    sokord = input()

    if sokord == "":
        print("Skriv nagot att soka pa.")
        return

    traffar = databas.sok_bok(sokord)
    if len(traffar) == 0:
        print("Inga traffar pa '" + sokord + "'.")
        return

    print("")
    print("--- Sokresultat (" + str(len(traffar)) + " st) ---")
    for rad in traffar:
        print(str(rad[0]) + ". " + rad[1] + " - " + rad[2])


def kor_visa_alla():
    bocker = databas.hamta_alla()
    if len(bocker) == 0:
        print("Inga bocker i biblioteket annu.")
        return

    print("")
    print("--- Alla bocker (" + str(len(bocker)) + " st) ---")
    i = 0
    while i < len(bocker):
        rad = bocker[i]
        print(str(rad[0]) + ". " + rad[1] + " - " + rad[2])
        i = i + 1


def main():
    databas.skapa_tabell()
    print("Valkommen till biblioteket!")

    fortsatt = True
    while fortsatt == True:
        val = visa_meny()

        if val == "1":
            kor_lagg_till()
        elif val == "2":
            kor_sok()
        elif val == "3":
            kor_visa_alla()
        elif val == "4":
            print("Hej da!")
            fortsatt = False
        else:
            print("Ogiltigt val, prova igen.")


main()
