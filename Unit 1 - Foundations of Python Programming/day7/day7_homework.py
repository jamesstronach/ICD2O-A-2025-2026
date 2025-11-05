# Question 1

import math
print(f"{math.pi:.3f}")

# Question 2

price = 29.99
print(f"${float(price):.2f}")

# Question 3
tax_rate = 0.075
print(f"{tax_rate:.2%}")

# Question 4

discount = 0.25
print(f"{discount:.1%}")

# Question 5

city = "New York"
print(f"{city:>15}")

# Question 6

temperature = 72.5
print(f"|{temperature:^10}|")

# Question 7

item = "128GB USB"
price = 29.99
quantity = 2
total = price*quantity
print(f"{"Item":^13}{"Price":>15}{"Quantity":>13}{"Total":>10}")
print(f"{item:>13}{price:>15}{quantity:>13}{total:>10}")

# Question 8

city = "Toronto"
population = "7,106,379"
area = "641 (sq km)"
print(f"{"City":^13}{"Population":>15}{"Area":>13}")
print(f"{city:>11}{population:>16}{area:>21}")