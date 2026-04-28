# Lararbedomd uppgift 2 - Hantera anvandardata
# Mohammad Sami Alsharef
# Programmering 2

# lista for alla anvandare
anvandare_lista = []


# lagga till anvandare i listan
def lagg_till_anvandare():
    global anvandare_lista
    
    print("")
    print("-- Lagg till ny anvandare --")
    print("")
    
    print("Skriv namn: ", end="")
    namn = input()
    
    # hamta alder fran anvandaren
    print("Skriv alder: ", end="")
    alder_text = input()
    alder = int(alder_text)
    
    print("Skriv e-post: ", end="")
    epost = input()
    
    # skapa dictonary med anvandare info (stavfel: dictionary)
    ny_anvandare = {}
    ny_anvandare["namn"] = namn
    ny_anvandare["alder"] = alder
    ny_anvandare["epost"] = epost
    
    anvandare_lista.append(ny_anvandare)
    
    print("")
    print("Anvandare tillagd!")
    # print("debug: " + str(ny_anvandare))


# soka anvandre i listan (stavfel: anvandare)
def sok_anvandare():
    global anvandare_lista
    
    print("")
    print("-- Sok anvandare --")
    print("")
    
    antal = len(anvandare_lista)
    if antal == 0:
        print("Inga anvandare finns i listan.")
        return
    
    print("Skriv sokord (namn eller epost): ", end="")
    sokord = input()
    
    sokord_lower = sokord.lower()
    
    # letar igenom hela listan
    hittade = []
    for anvandare in anvandare_lista:
        namn = anvandare["namn"]
        epost = anvandare["epost"]
        
        # gor om till smabokstaver sa det matchar
        namn_lower = namn.lower()
        epost_lower = epost.lower()
        
        if sokord_lower in namn_lower:
            hittade.append(anvandare)
        elif sokord_lower in epost_lower:
            hittade.append(anvandare)
    
    print("")
    antal_hittade = len(hittade)
    if antal_hittade == 0:
        print("Inga anvandare hittades.")
    else:
        print("Hittade " + str(antal_hittade) + " anvandare:")
        print("")
        for person in hittade:
            visa_en_anvandare(person)


# visa en anvandare (hjalp funktion)
def visa_en_anvandare(anvandare):
    namn = anvandare["namn"]
    alder = anvandare["alder"]
    epost = anvandare["epost"]
    
    print("Namn: " + namn)
    print("Alder: " + str(alder))
    print("E-post: " + epost)
    print("---")


# hjalpfunktion for sortering
def hamta_namn(anvandare):
    namn = anvandare["namn"]
    namn_lower = namn.lower()
    return namn_lower


# visa alla sorterat efter namn
def visa_alla_anvandare():
    global anvandare_lista
    
    print("")
    print("-- Alla anvandare --")
    print("")
    
    antal = len(anvandare_lista)
    if antal == 0:
        print("Inga anvandare finns i listan.")
        return
    
    # sortera med hjalp av funktoin (stavfel: funktion)
    # hittade detta pa stackoverflow
    sorterad_lista = sorted(anvandare_lista, key=hamta_namn)
    
    print("Totalt " + str(antal) + " anvandare:")
    print("")
    
    for anvandare in sorterad_lista:
        visa_en_anvandare(anvandare)


# meny funktoin
def visa_meny():
    print("")
    print("=== Anvandarhantering ===")
    print("1. Lagg till anvandare")
    print("2. Sok anvandare")
    print("3. Visa alla anvandare")
    print("4. Avsluta")
    print("")


# huvudprogram
def main():
    
    # TODO: kanske lagga till ta bort anvandare sen?
    
    fortsatt = True
    while fortsatt == True:
        
        visa_meny()
        
        print("Valj ett alternativ: ", end="")
        val = input()
        
        if val == "1":
            lagg_till_anvandare()
        elif val == "2":
            sok_anvandare()
        elif val == "3":
            visa_alla_anvandare()
        elif val == "4":
            print("")
            print("Programmet avslutas.")
            fortsatt = False
        else:
            print("Ogiltigt val, forsok igen.")


# starta
main()
