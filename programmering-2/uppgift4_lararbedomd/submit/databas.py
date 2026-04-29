# Mohammad Sami Alsharef
# databas-grejer for biblioteket

import sqlite3

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
