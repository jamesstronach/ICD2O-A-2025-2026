# Item      Quantity      Price($)
# Apples          12          0.75
# Bananas         20          0.60
# Oranges          8          2.50
# Cherries       123          4.41

item1 = "Apples"
item2 = "Bananas"
item3 = "Oranges"
item4 = "Cherries"

quantity1 = 12
quantity2 = 20
quantity3 = 8
quantity4 = 123

cost1 = 0.75
cost2 = 0.60
cost3 = 2.50
cost4 = 4.41

print(f"{"Item":<12}{"Quantity":>10}{"Price":>10}")
print(f"{item1:<12}{quantity1:>10}{cost1:>10}")
print(f"{item2:<12}{quantity2:>10}{cost2:>10}")
print(f"{item3:<12}{quantity3:>10}{cost3:>10}")
print(f"{item4:<12}{quantity4:>10}{cost4:>10}")
