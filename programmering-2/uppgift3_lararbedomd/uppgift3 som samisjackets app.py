# Mohammad Sami Alsharef
# GS samis jackets - shop programm


# base klass for products
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(self.name + " - " + str(self.price) + " SEK")


# Jacket inerhets from Product (arv)
class Jacket(Product):
    def __init__(self, name, price, size):
        Product.__init__(self, name, price)
        self.size = size

    def describe(self):
        print(self.name + " (" + self.size + ") - " + str(self.price) + " SEK")


# kund med membership nivaa
class Customer:
    def __init__(self, name, email, tier):
        self.name = name
        self.email = email
        self.tier = tier

    # raknar ut rabatten
    def get_discount(self):
        discount = 0
        if self.tier == "silver":
            discount = 5
        elif self.tier == "gold":
            discount = 10
        elif self.tier == "platinum":
            discount = 15
        # TODO: kanske lagga till VIP tier sen?
        return discount


# varukorg, lagrar det kunden lagger till
class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)
        print(product.name + " added to cart.")

    def show(self):
        if len(self.items) == 0:
            print("Cart is empty.")
            return
        print("")
        print("--- Your cart ---")
        i = 0
        while i < len(self.items):
            self.items[i].describe()
            i = i + 1

    def total(self):
        summa = 0
        for item in self.items:
            summa = summa + item.price
        # print("debug total: " + str(summa))
        return summa


def main():
    print("=== GS by Samis Jackets ===")
    print("")

    print("Enter your name: ", end="")
    name = input()

    print("Enter email: ", end="")
    email = input()

    print("Membership tier (bronze/silver/gold/platinum): ", end="")
    tier = input()

    customer = Customer(name, email, tier)
    # print("debug: " + customer.tier)
    cart = Cart()
    # TODO: kanske spara kundinfo till fil senare

    # produkter i lagret
    products = []
    products.append(Jacket("Black Puffer", 799, "M"))
    products.append(Jacket("Beige Trenchcoat", 1099, "L"))
    products.append(Jacket("Grey Hoodie", 499, "S"))
    products.append(Jacket("Winter Parka", 1299, "XL"))
    # products.append(Jacket("test jacket", 1, "S"))  tog bort

    fortsatt = True
    while fortsatt == True:

        print("")
        print("1. Show products")
        print("2. Add to cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        print("> ", end="")
        choice = input()

        if choice == "1":
            print("")
            i = 0
            while i < len(products):
                print(str(i) + ". ", end="")
                products[i].describe()
                i = i + 1

        elif choice == "2":
            print("Product number: ", end="")
            nr_text = input()
            nr = int(nr_text)
            if nr >= 0 and nr < len(products):
                cart.add(products[nr])
            else:
                print("Invalid number.")

        elif choice == "3":
            cart.show()

        elif choice == "4":
            cart.show()
            if len(cart.items) == 0:
                print("Nothing to checkout.")
            else:
                total = cart.total()
                discount = customer.get_discount()
                saved = int(total * discount / 100)
                final = total - saved
                print("")
                print("Customer: " + customer.name)
                print("Tier: " + customer.tier + " (" + str(discount) + "% discount)")
                print("Total: " + str(total) + " SEK")
                print("You save: " + str(saved) + " SEK")
                print("To pay: " + str(final) + " SEK")
                print("")
                print("Order placed! Thank you for shopping.")
                fortsatt = False

        elif choice == "5":
            fortsatt = False

        else:
            print("Invalid choice.")


main()
