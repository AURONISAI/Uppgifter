# Mohammad Sami Alsharef

namn = ""
alder = 0

def registrera():
    global namn
    global alder
    
    print("Enter name: ", end="")
    inmatat_namn = input()
    namn = inmatat_namn
    
    print("Enter age: ", end="")
    inmatat_alder = input()
    alder = int(inmatat_alder)


def visa_hundra():
    global namn
    global alder
    
    if namn == "":
        print("Registera forst!")
    else:
        ar_nu = 2026
        ar_kvar = 100 - alder
        ar_hundra = ar_nu + ar_kvar
        print(namn + ", you will turn 100 in the year " + str(ar_hundra) + ".")


def visa_meny():
    print("1. Enter your name and age")
    print("2. Show when you will turn 100")
    print("3. Exit")


def main():
    fortsatt = True
    
    while fortsatt == True:
        visa_meny()
        
        print("> ", end="")
        val = input()
        
        if val == "1":
            registrera()
            print("")
        elif val == "2":
            visa_hundra()
            print("")
        elif val == "3":
            fortsatt = False
        else:
            print("Fel val!")
            print("")


main()
