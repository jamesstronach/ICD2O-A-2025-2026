# Prints the welcome banner for the shop
# Parameters: none
# Returns: nothing
def show_banner():
    print("🍓 Welcome to The Smoothie Shack! 🍌")

# Calculates the total cost of a smoothie order
# Parameters: base_price (float), num_toppings (int)
# Returns: total cost (float)
def calculate_cost(base_price, num_toppings):
    return base_price + (num_toppings * 0.75)

# Prints the final receipt for the customer
# Parameters: name (string), smoothie (string), total (float)
# Returns: nothing
def print_receipt(name, smoothie, total):
    print(name + " ordered a " + smoothie + " smoothie.")
    print("Total: $" + str(round(total, 2)))

# Converts ounces to millilitres
# Parameters: ounces (float)
# Returns: millilitres (float)
def ounces_to_ml(ounces):
    return ounces * 29.5735

show_banner()
customer_name = "D-Lo"
smoothie_type = "Mango Pineapple"

price = calculate_cost(4.50, 3)

print_receipt(customer_name, smoothie_type, price)

oz = 16
smoothie_in_ml = ounces_to_ml(oz)

print(f"{oz}oz is {smoothie_in_ml} mL")

