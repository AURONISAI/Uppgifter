# Lärarbedömd uppgift 3
Mohammad Sami Alsharef

## Valt alternativ
**Alternativ 1 (eget) – baserat på vår riktiga app G&S by Samis Jackets**

## Klasser
- `Product` – basklass med name och price
- `Jacket(Product)` – ärver Product, lägger till size och egen describe()
- `Customer` – namn, email, membership tier + get_discount()
- `Cart` – lista med produkter, add, show, total

## Design
```
Product
└── Jacket  (arv, lägger till size)

Customer    (separat, hanterar rabatt baserat på tier)
Cart        (separat, lista av Product-objekt)
```

## Hur det fungerar
1. Kunden anger namn, email, membership tier
2. Ser produktlistan (jackor med storlek och pris)
3. Lägger till i varukorgen
4. Checkar ut – rabatt räknas automatiskt baserat på tier
5. bronz = 0%, silver = 5%, gold = 10%, platinum = 15%

## Problem jag hade
- Glömde att anropa Product.__init__() i Jacket-klassen i början
- Osäker på hur rabatt ska räknas, använde int() för att avrunda

## Källor
- vår app (src/types/user.ts och cart.ts)
- w3schools arv i Python
