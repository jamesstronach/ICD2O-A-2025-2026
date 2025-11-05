drink = input("Please enter the cost of your drink: ")
appetizer = input("Please enter the cost of your appetizer: ")
entree = input("Please enter the cost of your entree: ")
dessert = input("Please enter the cost of your dessert ")

drink = float(drink)
appetizer = float(appetizer)
entree = float(entree)
dessert = float(dessert)

subtotal = drink + appetizer + entree + dessert
total = subtotal*1.15
print("The subtotal of your meal is: $", subtotal)
print("The tip amount of your meal is: $", subtotal*0.15)
print("The total cost of your meal is: $", total)

