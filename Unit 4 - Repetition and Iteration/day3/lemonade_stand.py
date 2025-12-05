import random

gameover = False

def introscreen():
    print("HI! WELCOME TO LEMONSVILLE CALIFORNIA!\nIN THIS SMALL TOWN, YOU ARE IN CHARGE OF RUNNING YOUR OWN LEMONADE STAND. YOU CAN\n COMPETE WITH ONLY YOURSELF BECAUSE I SUCK AT CODING\n, BUT HOW MUCH PROFIT YOU MAKE IS UP TO YOU.\n ARE YOU STARTING A NEW GAME? (YES OR NO)")
    newgame = ""
    
    while newgame != "Yes" or newgame != "No":
        newgame = input("TYPE YOUR ANSWER AND HIT RETURN (\"Yes\" or \"No\") ==> ")
        if newgame == "Yes":
            day = 1
            money = 200
            return money, day
        elif newgame == "No":
            day = int(input("What day was it the last time you played? "))
            money = -1
            while money <=0:
                money = int(input("How much money did you have? "))
                if money <= 0:
                    print("Not a valid amount!")
            return money, day

def decisions(money, day):
    print("Day", day)
    print("Money:", money)

    sign_cost = 15
    weathers = ["Sunny", "Cloudy", "Hot and Dry"]
    weather = random.choice(weathers)

    print("The weather is", weather)

    if weather == "Sunny":
        glass_cost = random.randint(3,4)
    elif weather == "Cloudy":
        glass_cost = random.randint(1,2)
    elif weather == "Hot and Dry":
        glass_cost = random.randint(4,5)

    print("Glass Cost:", glass_cost)

    glasses = int(input("How many glasses would you like to make? "))

    while glasses*glass_cost > money:
        print("You don't have that much money as you only have ",money, "cents")
        glasses = int(input("How many glasses would you like to make? "))

    money -= glasses*glass_cost

    signs = int(input("How many signs would you like to make? "))

    while signs*sign_cost > money:
        print("You don't have that much money as you only have ",money, "cents")
        signs = int(input("How many signs would you like to make? "))

    money -= signs*sign_cost

    glass_price = int(input("How much money would you like to sell your lemonade for (in cents) "))

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

    rounded_glasses_sold = int(glasses_sold)

    money -= glasses*2
    money -= signs*15
    money += rounded_glasses_sold*glass_price
    print("Glasses Sold:", rounded_glasses_sold)

    return money

money, day = introscreen()

while gameover == False:
    glasses, signs, glass_price, money, weather = decisions(money, day)
    money = sold(glasses, signs, glass_price, money, weather)
    print("-"*100)
    day+=1
    if money <= 0:
        gameover = True
        print("YOU BROKE DUMBAHH. GO DO BEP2O STOOPIDD")