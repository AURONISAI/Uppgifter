# Mohammad Sami Alsharef



anvandare_lista = []


def lagg_till_anvandare():
    global anvandare_lista
    
    print("")
    print("-- Add new user --")
    print("")
    
    print("Enter name: ", end="")
    namn = input()
   
    print("Enter age: ", end="")
    alder_text = input()
    alder = int(alder_text)
    
    print("Enter email: ", end="")
    epost = input()
    
    ny_anvandare = {}
    ny_anvandare["namn"] = namn
    ny_anvandare["alder"] = alder
    ny_anvandare["epost"] = epost
    
    anvandare_lista.append(ny_anvandare)
    
    print("")
    print("User added!")
 


def sok_anvandare():
    global anvandare_lista
    
    print("")
    print("-- Search user --")
    print("")
    
    antal = len(anvandare_lista)
    if antal == 0:
        print("No users in the list.")
        return
    
    print("Enter search word (name or email): ", end="")
    sokord = input()
    
    sokord_lower = sokord.lower()
    
 
    hittade = []
    for anvandare in anvandare_lista:
        namn = anvandare["namn"]
        epost = anvandare["epost"]
        
        namn_lower = namn.lower()
        epost_lower = epost.lower()
        
        if sokord_lower in namn_lower:
            hittade.append(anvandare)
        elif sokord_lower in epost_lower:
            hittade.append(anvandare)
    
    print("")
    antal_hittade = len(hittade)
    if antal_hittade == 0:
        print("No users found.")
    else:
        print("Found " + str(antal_hittade) + " user(s):")
        print("")
        for person in hittade:
            visa_en_anvandare(person)


def visa_en_anvandare(anvandare):
    namn = anvandare["namn"]
    alder = anvandare["alder"]
    epost = anvandare["epost"]
    
    print("Name: " + namn)
    print("Age: " + str(alder))
    print("Email: " + epost)
    print("---")


def hamta_namn(anvandare):
    namn = anvandare["namn"]
    namn_lower = namn.lower()
    return namn_lower


def visa_alla_anvandare():
    global anvandare_lista
    
    print("")
    print("-- All users --")
    print("")
    
    antal = len(anvandare_lista)
    if antal == 0:
        print("No users in the list.")
        return
    
    sorterad_lista = sorted(anvandare_lista, key=hamta_namn)
    
    print("Total " + str(antal) + " user(s):")
    print("")
    
    for anvandare in sorterad_lista:
        visa_en_anvandare(anvandare)



def visa_meny():
   
    meny_rader = (
        "1. Add user",
        "2. Search user",
        "3. Show all users",
        "4. Exit"
    )
    
    print("")
    print("=== User Management ===")
    for rad in meny_rader:
        print(rad)
    print("")



def main():
    
    
    fortsatt = True
    while fortsatt == True:
        
        visa_meny()
        
        print("Choose an option: ", end="")
        val = input()
        
        if val == "1":
            lagg_till_anvandare()
        elif val == "2":
            sok_anvandare()
        elif val == "3":
            visa_alla_anvandare()
        elif val == "4":
            print("")
            print("Program is closing.")
            fortsatt = False
        else:
            print("Invalid choice, try again.")



main()
# todo later mybe to make it real workign by conecting to maria data base in one.com and use it to our coustmer database 
