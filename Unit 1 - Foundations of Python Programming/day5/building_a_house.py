# I suck at math so this is wrong but the code works.
# This code is NOT optomized. I could've just said float infront of the inputs.

house_l = input("Please enter the length of one of the walls of the house (in metres): ")
house_w = input("Please enter the width of one of the walls of the house (in metres): ")
house_h = input("Please enter the height of one of the walls of the house(in metres): ")
b = input("Please enter the cost of a brick: $")
bl = input("Please enter the length of a brick: ")
bw = input("Please enter the width of a brick: ")
bh = input("Please enter the height of a brick: ")

house_l = float(house_l)
house_w = float(house_w)
house_h = float(house_h)
b = float(b)
bl = float(bl)
bw = float(bw)
bh = float(bh)

house_sa = house_l*house_w
brick_sa = bl*bw
bricks = house_sa/brick_sa

all_b = bricks*b

print("The surface area of all the walls is: ", house_sa, "square metres")
print("The number of bricks required is: ", bricks, "bricks")
print("The total cost of bricks is: $", all_b)