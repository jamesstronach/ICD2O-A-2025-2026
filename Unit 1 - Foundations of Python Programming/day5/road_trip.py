distance = float(input("What is the distance of your trip in kilometres? "))
fuel_efficiency = float(input("What is the fuel efficiency of your vehicle in kilometres per liter? "))
price = float(input("What is the current price of fuel per liter? "))
people = float(input("How many people are in the vehicle? "))

fuel_needed = distance/fuel_efficiency
fuel_cost = price*fuel_needed
fuel_per_passenger = fuel_cost/people

print(f"The total amount of fuel needed for the trip is {fuel_needed} liters. The total cost of fuel for the trip is ${fuel_cost}. The cost of fuel per passenger is ${fuel_per_passenger}.")