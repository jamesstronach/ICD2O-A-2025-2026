import random

gameover = False
def introscreen():
    print("HI! WELCOME TO LEMONSVILLE CALIFORNIA!\nIN THIS SMALL TOWN, YOU ARE IN CHARGE OF RUNNING YOUR OWN LEMONADE STAND. YOU CAN\n COMPETE WITH ONLY YOURSELF BECAUSE I SUCK AT CODING\n, BUT HOW MUCH PROFIT YOU MAKE IS UP TO YOU.\n ARE YOU STARTING A NEW GAME? (YES OR NO)")
    newgame = input("TYPE YOUR ANSWER AND HIT RETURN ==> ")
    if newgame == ("Yes".lower):
        day = 0
        return True, day
    elif newgame == ("No".lower):
        return False
    elif newgame == False:
        day = int(input("What day was it the last time you played? "))
        money = int(input("How much money did you have? "))
        return day, money
    else:
        # Bring us back to asking

def decisions(money, day):
    print("Day", day)
    print("Money:", money)
    glass_cost = 2
    sign_cost = 15
    weathers = ["Sunny", "Cloudy", "Hot and Dry"]
    weather = random.choice(weathers)

    print("The weather is", weather)

    glasses = int(input("How many glasses would you like to make? "))

    while glasses*glass_cost > money:
        print("You don't have that much money as you only have ",money, "cents")
        glasses = int(input("How many glasses would you like to make? "))

    signs = int(input("How many signs would you like to make? "))
    money -= signs*sign_cost

    glass_price = int(input("How much money would you like to sell your lemonade for (in cents)"))
  
    return glasses, signs, glass_price, money, weather

# returns how much money you have left
def sold(glasses, signs, glass_price, money, weather):
# need to incorporate signs into the equasion
    if weather == "Sunny" and glass_price <= 18:
        glasses_sold = random.randint(40, 78)*0.01*glasses
    elif weather == "Sunny" and glass_price >= 18:
        glasses_sold = random.randint(40, 57)*0.01*glasses
    elif weather == "Cloudy" and glass_price >= 5:
        glasses_sold = random.randint(10, 20)*0.01*glasses
    elif weather == "Cloudy" and glass_price <= 5:
        glasses_sold = random.randint(20, 40)*0.01*glasses
    elif weather == "Hot and Dry" and glass_price >= 25:
        glasses_sold = random.randint(67, 80)*0.01*glasses
    elif weather == "Hot and Dry" and glass_price <= 25:
        glasses_sold = random.randint(80, 100)*0.01*glasses # and don't just make it percentage because what if they make like 2 glasses, they're gonna sell out ofc

    money -= glasses*2
    money -= signs*15
    money += glasses_sold*glass_price
    print("Glasses Sold:", glasses_sold)

while gameover == False:
    glasses, signs, glass_price, money, weather = decisions(money, day)
    money = sold(glasses, signs, glass_price, money, weather)
    day+=1