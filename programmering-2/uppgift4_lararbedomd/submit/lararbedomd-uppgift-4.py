# Mohammad Sami Alsharef
# bibliotekssystem lararbedomd 4

import sqlite3
import os

DB_FIL = "bibliotek.db"


def skapa_tabell():
    try:
        koppling = sqlite3.connect(DB_FIL)
        cur = koppling.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS bocker ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "titel TEXT NOT NULL, "
                    "forfattare TEXT NOT NULL)")
        koppling.commit()
        koppling.close()
    except Exception as fel:
        print("Kunde inte skapa tabell: " + str(fel))


def lagg_till_bok(titel, forfattare):
    try:
        koppling = sqlite3.connect(DB_FIL)
        cur = koppling.cursor()
        # ? istallet for att klistra in text - sql injection
        cur.execute("INSERT INTO bocker (titel, forfattare) VALUES (?, ?)",
                    (titel, forfattare))
        koppling.commit()
        koppling.close()
        return True
    except Exception as fel:
        print("Fel nar boken sparades: " + str(fel))
        return False


def hamta_alla():
    bocker = []
    try:
        koppling = sqlite3.connect(DB_FIL)
        cur = koppling.cursor()
        cur.execute("SELECT id, titel, forfattare FROM bocker ORDER BY id")
        bocker = cur.fetchall()
        koppling.close()
    except Exception as fel:
        print("Fel vid hamtning: " + str(fel))
    return bocker


def sok_bok(sokord):
    traffar = []
    try:
        koppling = sqlite3.connect(DB_FIL)
        cur = koppling.cursor()
        monster = "%" + sokord + "%"
        cur.execute("SELECT id, titel, forfattare FROM bocker "
                    "WHERE titel LIKE ? OR forfattare LIKE ?",
                    (monster, monster))
        traffar = cur.fetchall()
        koppling.close()
    except Exception as fel:
        print("Fel vid sokningen: " + str(fel))
    return traffar


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

    ok = lagg_till_bok(titel, forfattare)
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

    traffar = sok_bok(sokord)
    if len(traffar) == 0:
        print("Inga traffar pa '" + sokord + "'.")
        return

    print("")
    print("--- Sokresultat (" + str(len(traffar)) + " st) ---")
    for rad in traffar:
        print(str(rad[0]) + ". " + rad[1] + " - " + rad[2])


def kor_visa_alla():
    bocker = hamta_alla()
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
    skapa_tabell()
    print("Valkommen till biblioteket!")
    # print("debug db: " + os.path.abspath(DB_FIL))

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
