# Inputs
US_classrooms = int(input("How many classrooms are in the Upper School? "))
water_fountains = int(input("How many student water fountains? "))
restrooms = int(input("How many student restrooms? "))
microwaves = int(input("How many microwaves? "))

# Density
water_fountains_density = water_fountains/US_classrooms
restrooms_density = restrooms/US_classrooms
microwaves_density = microwaves/US_classrooms

# Condition
water_fountains_condition = input("Condition of fountains? ")
restrooms_condition = input("Condition of restrooms? ")
microwaves_condition = input("Condition of microwaves? ")

print(f"\nResults")
print(f"-------")
print(f"Fountains per classroom: {round(water_fountains_density,2)} (Condition: {water_fountains_condition})")
print(f"Restrooms per classroom: {round(restrooms_density)} (Condition: {restrooms_condition})")
print(f"Microwaves per classroom: {round(microwaves_density)} (Condition: {microwaves_condition})")

print("\nThanks for helping map our Upper School resources!")

# 1. We can see how many utilities there are in the school compared to the amount of classrooms.
# 2. I would add counting students to see how many students share the same utilities.