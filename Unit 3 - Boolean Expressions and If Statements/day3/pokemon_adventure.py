import random
player = input("What is your name? ")

print("-"*100)

def choose_pokemon():
    print("1 = Sprigatito, 2 = Fuecoco, 3 = Quaxly")
    pokemon_starters = (input("Enter the number of your pokemon: "))
    if pokemon_starters == "1":
        pokemon_starters = "Sprigatito"
    elif pokemon_starters == "2":
        pokemon_starters = "Fuecoco"
    elif pokemon_starters == "3":
        pokemon_starters = "Quaxly"
    else:
        print("Invalid")
        exit()
    

    return pokemon_starters 
starter_pokemon = choose_pokemon()

print("-"*100)

print("You chose", starter_pokemon) 

print("-"*100)

rival = input("What is your best friend/rivals name? ")

print("-"*100)

def choose_rival_starter_pokemon():
    if starter_pokemon == "Sprigatito":
        rival_starter_pokemon_choice = "Quaxly"
    elif starter_pokemon == "Fuecoco":
        rival_starter_pokemon_choice = "Sprigatito"
    elif starter_pokemon == "Quaxly":
        rival_starter_pokemon_choice = "Fuecoco"
    else:
        print("Invalid")
        exit()

    return rival_starter_pokemon_choice
rival_starter_pokemon = choose_rival_starter_pokemon()

def starter_pokemon_intro(starter_pokemon):
    if starter_pokemon == "Sprigatito":
        return f"{starter_pokemon}, is a grass type pokemon and is a quadrupedal feline Pokémon covered in pale green fur. The fur's composition is similar to that of plants, allowing it to absorb sunlight for energy. It has green ears with pale green insides, a tuft of fur on the front of its chest and a green marking around its pink eyes and nose that resemble leaves. When its mouth is open, two pointed teeth can be seen in its upper jaw. It has a fluffy tail and small paws with pink paw pads underneath and no visible toes. Eventually, this little feline friend will join the darkside and take on a far stronger role"
    elif starter_pokemon == "Fuecoco":
        return f"{starter_pokemon}, is a fire pokemon that came from the woods. After it was born, it was the most playful and cheerful pokemon known to the school that hosts the disastrous, TEAM STAR. One day, it will become a crocodile that will destroy everything in its path with its amazing singing voice."
    elif starter_pokemon == "Quaxly":
        return f"{starter_pokemon}, Quaxly is a water type pokemon and is a white duckling-like Pokémon. It has a yellow beak and blue eyes. It has teal webbed feet and a large teal coif-like crest that covers its head, with a feathery tuft in the front and a white curvy line shaped like a wave. Quaxly's coif has a smooth feel thanks to the rich, moist cream that holds it. The cream it secretes can repel grime. The coif can become unkempt should it get dry."
print(starter_pokemon_intro(starter_pokemon))

print("-"*100)

def player_intro(player, starter_pokemon):
    print (f"Welcome to the world of pokemon, {player}. I'm sure you and your {starter_pokemon} will make a great team. You've just turned 10 years old, growing up in the middle of nowhere in the woods, and you're ready to explore the world, but not so fast. Your rival {rival} is trying to beat you and you need to prove you're better than him to fulfill your superiority complex." )

print(player_intro(player, starter_pokemon))

print("-"*100)

print(f"You start walking 2 kilometres away from your house, further than you've ever gone and you can see a city in the distance. Do you go to the city? Or walk another direction towards more wild and tall grass?")
walking_towards = input("Do you go to the city? Or walk another direction towards more wild and tall grass? (1 is city, 2 and others is grass)")

def make_decision():
    if walking_towards == "1":
        print("As you're walking towards the city, you encounter your best friend.")
        return "1"
    elif walking_towards == "2":
        print("You walk towards the plains and encounter a wild scyther.")
        return "2"
    else:
        print("Invalid")
        exit()
encounter = make_decision()

if starter_pokemon == "Fuecoco":
    l1_starter_pokemon_HP = 67
elif starter_pokemon == "Sprigatito":
    l1_starter_pokemon_HP = 40
elif starter_pokemon == "Quaxly":
    l1_starter_pokemon_HP = 55

if rival_starter_pokemon == "Fuecoco":
    l1_rival_starter_pokemon_HP = 67
elif rival_starter_pokemon == "Sprigatito":
    l1_rival_starter_pokemon_HP = 40
elif rival_starter_pokemon == "Quaxly":
    l1_rival_starter_pokemon_HP = 55

def rival_battle(starter_pokemon):
    global l1_rival_starter_pokemon_HP, l1_starter_pokemon_HP
    opponent_defense_lower = 0
    opponent_attack_lower = 0
    print("-"*100)
    print (f"Beginning battle with {rival}.\n{starter_pokemon} HP: {l1_starter_pokemon_HP}\nRival: {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    print("-"*100)
    if starter_pokemon == "Fuecoco":
        print("1 = Tackle | 2 = Ember | 3 = Leer")
    elif starter_pokemon == "Sprigatito":
        print("1 = Leafage | 2 = Scratch | 3 = Tail Whip")
    elif starter_pokemon == "Quaxly":
        print("1 = Pound | 2 = Water Gun | 3 = Growl")
    move1 = input("What move would you like to use? ")

    if starter_pokemon == "Fuecoco" and move1 == "1" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move1 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move1 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move1 == "1" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move1 == "2" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move1 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move1 == "1" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move1 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move1 == "3" and opponent_attack_lower == 0:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 1

    print("-"*100)

    if l1_rival_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*-100}")
        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*0.1}")
        return "Lost"

    print("-"*100)

    if rival_starter_pokemon == "Fuecoco" and opponent_attack_lower == 0:
        print(f"{rival_starter_pokemon} used Tackle")
        l1_starter_pokemon_HP -= 12
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Sprigatito" and opponent_attack_lower == 0:
        l1_starter_pokemon_HP -= 12
        print(f"{rival_starter_pokemon} used Scratch")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Quaxly" and opponent_attack_lower == 0:
        l1_starter_pokemon_HP -= 12
        print(f"{rival_starter_pokemon} used Pound")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")

    if rival_starter_pokemon == "Fuecoco" and opponent_attack_lower == 1:
        print(f"{rival_starter_pokemon} used Tackle")
        l1_starter_pokemon_HP -= 8
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Sprigatito" and opponent_attack_lower == 1:
        l1_starter_pokemon_HP -= 8
        print(f"{rival_starter_pokemon} used Scratch")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Quaxly" and opponent_attack_lower == 1:
        l1_starter_pokemon_HP -= 8
        print(f"{rival_starter_pokemon} used Pound")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")

    if l1_rival_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*-100}")
        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*0.1}")
        return "Lost"

    print("-"*100)

    move2 = input("What move would you like to use? ")
    if starter_pokemon == "Fuecoco" and move2 == "1" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 17
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move2 == "2" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 40
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move2 == "3" and opponent_defense_lower == 1:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Sprigatito" and move2 == "1" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 40
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move2 == "2" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 17
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move2 == "3" and opponent_defense_lower == 1:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Quaxly" and move2 == "1" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 17
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move2 == "2" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 40
        print("It's Super Effective!")
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move2 == "3" and opponent_attack_lower == 1:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 2

    elif starter_pokemon == "Fuecoco" and move2 == "1" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move2 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move2 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move2 == "1" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move2 == "2" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move2 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move2 == "1" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move2 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move2 == "3" and opponent_attack_lower == 0:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 1

    print("-"*100)

    if rival_starter_pokemon == "Fuecoco" and opponent_attack_lower == 0:
        print(f"{rival_starter_pokemon} used Tackle")
        l1_starter_pokemon_HP -= 12
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Sprigatito" and opponent_attack_lower == 0:
        l1_starter_pokemon_HP -= 12
        print(f"{rival_starter_pokemon} used Scratch")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Quaxly" and opponent_attack_lower == 0:
        l1_starter_pokemon_HP -= 12
        print(f"{rival_starter_pokemon} used Pound")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")

    if rival_starter_pokemon == "Fuecoco" and opponent_attack_lower == 1:
        print(f"{rival_starter_pokemon} used Tackle")
        l1_starter_pokemon_HP -= 8
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Sprigatito" and opponent_attack_lower == 1:
        l1_starter_pokemon_HP -= 8
        print(f"{rival_starter_pokemon} used Scratch")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Quaxly" and opponent_attack_lower == 1:
        l1_starter_pokemon_HP -= 8
        print(f"{rival_starter_pokemon} used Pound")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")

    if rival_starter_pokemon == "Fuecoco" and opponent_attack_lower == 2:
        print(f"{rival_starter_pokemon} used Tackle")
        l1_starter_pokemon_HP -= 5
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Sprigatito" and opponent_attack_lower == 2:
        l1_starter_pokemon_HP -= 5
        print(f"{rival_starter_pokemon} used Scratch")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Quaxly" and opponent_attack_lower == 2:
        l1_starter_pokemon_HP -= 5
        print(f"{rival_starter_pokemon} used Pound")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")

    if l1_rival_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*-100}")
        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*0.1}")
        return "Lost"

    print("-"*100)

    move3 = input("What move would you like to use? ")
    if starter_pokemon == "Fuecoco" and move3 == "1" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move3 == "1" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "2" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move3 == "1" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "3" and opponent_attack_lower == 0:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 1

    elif starter_pokemon == "Fuecoco" and move3 == "1" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 17
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "2" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 40
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "3" and opponent_defense_lower == 1:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Sprigatito" and move3 == "1" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 40
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "2" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 17
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "3" and opponent_defense_lower == 1:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Quaxly" and move3 == "1" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 17
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "2" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 40
        print("It's Super Effective!")
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "3" and opponent_attack_lower == 1:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 2

    elif starter_pokemon == "Fuecoco" and move3 == "1" and opponent_defense_lower == 2:
        l1_rival_starter_pokemon_HP -= 25
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "2" and opponent_defense_lower == 2:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 70
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "3" and opponent_defense_lower == 2:
        print("The opponents defense is the lowest it can be.")
    elif starter_pokemon == "Sprigatito" and move3 == "1" and opponent_defense_lower == 2:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 70
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "2" and opponent_defense_lower == 2:
        l1_rival_starter_pokemon_HP -= 25
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "3" and opponent_defense_lower == 2:
        print("The opponents defense is the lowest it can be.")
    elif starter_pokemon == "Quaxly" and move3 == "1" and opponent_defense_lower == 2:
        l1_rival_starter_pokemon_HP -= 25
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "2" and opponent_defense_lower == 2:
        l1_rival_starter_pokemon_HP -= 70
        print("It's Super Effective!")
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "3" and opponent_attack_lower == 2:
        print("The opponents attack is the lowest it can be.")

    if l1_rival_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*-100}")
        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*0.1}")
        return "Lost"
    
    print("-"*100)

    if rival_starter_pokemon == "Fuecoco" and opponent_attack_lower == 0:
        print(f"{rival_starter_pokemon} used Tackle")
        l1_starter_pokemon_HP -= 12
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Sprigatito" and opponent_attack_lower == 0:
        l1_starter_pokemon_HP -= 12
        print(f"{rival_starter_pokemon} used Scratch")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Quaxly" and opponent_attack_lower == 0:
        l1_starter_pokemon_HP -= 12
        print(f"{rival_starter_pokemon} used Pound")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
        
    if rival_starter_pokemon == "Fuecoco" and opponent_attack_lower == 1:
        print(f"{rival_starter_pokemon} used Tackle")
        l1_starter_pokemon_HP -= 8
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Sprigatito" and opponent_attack_lower == 1:
        l1_starter_pokemon_HP -= 8
        print(f"{rival_starter_pokemon} used Scratch")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Quaxly" and opponent_attack_lower == 1:
        l1_starter_pokemon_HP -= 8
        print(f"{rival_starter_pokemon} used Pound")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")

    if rival_starter_pokemon == "Fuecoco" and opponent_attack_lower == 2:
        print(f"{rival_starter_pokemon} used Tackle")
        l1_starter_pokemon_HP -= 5
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Sprigatito" and opponent_attack_lower == 2:
        l1_starter_pokemon_HP -= 5
        print(f"{rival_starter_pokemon} used Scratch")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Quaxly" and opponent_attack_lower == 2:
        l1_starter_pokemon_HP -= 5
        print(f"{rival_starter_pokemon} used Pound")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")

    if l1_rival_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*-100}")
        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*0.1}")
        return "Lost"

    print("-"*100)

    move4 = input("What move would you like to use? ")
    if starter_pokemon == "Fuecoco" and move4 == "1" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move4 == "1" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "2" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move4 == "1" and opponent_defense_lower == 0:
        l1_rival_starter_pokemon_HP -= 12
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 30
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "3" and opponent_attack_lower == 0:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 1

    elif starter_pokemon == "Fuecoco" and move4 == "1" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 17
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "2" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 40
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "3" and opponent_defense_lower == 1:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Sprigatito" and move4 == "1" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 40
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "2" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 17
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "3" and opponent_defense_lower == 1:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Quaxly" and move4 == "1" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 17
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "2" and opponent_defense_lower == 1:
        l1_rival_starter_pokemon_HP -= 40
        print("It's Super Effective!")
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "3" and opponent_attack_lower == 1:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 2

    elif starter_pokemon == "Fuecoco" and move4 == "1" and opponent_defense_lower == 2:
        l1_rival_starter_pokemon_HP -= 25
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "2" and opponent_defense_lower == 2:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 70
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "3" and opponent_defense_lower == 2:
        print("The opponents defense is the lowest it can be.")
    elif starter_pokemon == "Sprigatito" and move4 == "1" and opponent_defense_lower == 2:
        print("It's Super Effective!")
        l1_rival_starter_pokemon_HP -= 70
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "2" and opponent_defense_lower == 2:
        l1_rival_starter_pokemon_HP -= 25
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "3" and opponent_defense_lower == 2:
        print("The opponents defense is the lowest it can be")
    elif starter_pokemon == "Quaxly" and move4 == "1" and opponent_defense_lower == 2:
        l1_rival_starter_pokemon_HP -= 25
        print(f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "2" and opponent_defense_lower == 2:
        l1_rival_starter_pokemon_HP -= 70
        print("It's Super Effective!")
        print (f"Rival {rival_starter_pokemon} HP: {l1_rival_starter_pokemon_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "3" and opponent_attack_lower == 2:
        print("The opponents attack is the lowest it can be.")

    if l1_rival_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        return "Lost"

    print("-"*100)

    if rival_starter_pokemon == "Fuecoco" and opponent_attack_lower == 0:
        print(f"{rival_starter_pokemon} used Tackle")
        l1_starter_pokemon_HP -= 12
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Sprigatito" and opponent_attack_lower == 0:
        l1_starter_pokemon_HP -= 12
        print(f"{rival_starter_pokemon} used Scratch")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Quaxly" and opponent_attack_lower == 0:
        l1_starter_pokemon_HP -= 12
        print(f"{rival_starter_pokemon} used Pound")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
        
    if rival_starter_pokemon == "Fuecoco" and opponent_attack_lower == 1:
        print(f"{rival_starter_pokemon} used Tackle")
        l1_starter_pokemon_HP -= 8
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Sprigatito" and opponent_attack_lower == 1:
        l1_starter_pokemon_HP -= 8
        print(f"{rival_starter_pokemon} used Scratch")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    elif rival_starter_pokemon == "Quaxly" and opponent_attack_lower == 1:
        l1_starter_pokemon_HP -= 8
        print(f"{rival_starter_pokemon} used Pound")
        print(f"{starter_pokemon} HP: {l1_starter_pokemon_HP}")
    
    if l1_rival_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*-100}")
        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {l1_rival_starter_pokemon_HP*0.1}")
        return "Lost"
           
    print("-"*100)

    # List a bunch of moves that do damage and add a catching mechanic. If we defeat, starter gets level 2. If we catch them, we add the scyther to our team.

def scyther_encounter(starter_pokemon):
    scyther_HP = 50
    global l1_starter_pokemon_HP
    opponent_defense_lower = 0
    opponent_attack_lower = 0
    score = 0
    print("-"*100)
    print(f"Beginning Scyther Encounter\n{starter_pokemon} HP: {l1_starter_pokemon_HP}\nScyther HP: {scyther_HP}")
    print("-"*100)

    throw_ball = input("What do you want to do? (1 for Throw Pokeball, 2 for Fight, 3 for Flee)")
    if throw_ball == "1" and scyther_HP == 50:
        print("The scyther escaped the ball and forced you into a fight.")
    elif throw_ball == "1" and scyther_HP < 50:
        print("You successfully caught the scyther")
        outcomes = ('curveball', 'no_curveball')
        chances = (0.5, 0.5)
        result = random.choices(outcomes, chances=chances, k=1)[0]
        if result == 'curveball':
            score = 5000
        return "Caught"
    elif throw_ball == "2":
        print("-"*100)
    elif throw_ball == "3":
        print("You successfully fled the scyther.")
        return "Fled"

    if starter_pokemon == "Fuecoco":
        print("1 = Tackle | 2 = Ember | 3 = Leer")
    elif starter_pokemon == "Sprigatito":
        print("1 = Leafage | 2 = Scratch | 3 = Tail Whip")
    elif starter_pokemon == "Quaxly":
        print("1 = Pound | 2 = Water Gun | 3 = Growl")

    move1 = input("What move would you like to use? ")
    if starter_pokemon == "Fuecoco" and move1 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move1 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        scyther_HP -= 30
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move1 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move1 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 15
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move1 == "2" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move1 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move1 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move1 == "2" and opponent_defense_lower == 0:
        print("It's Not Very Effective.")
        scyther_HP -= 8
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move1 == "3" and opponent_attack_lower == 0:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 1

    print("-"*100)

    if scyther_HP > 0 and opponent_attack_lower == 0:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 7
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 1:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 5
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)

    print("-"*100)

    if scyther_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {scyther_HP*-100} + {score}")

        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {scyther_HP*0.1+{score}}")
        return "Lost"
    
    print("-"*100)

    throw_ball = input("What do you want to do? (1 for Throw Pokeball, 2 for Fight, 3 for Flee)")
    if throw_ball == "1" and scyther_HP == 50:
        print("The scyther escaped the ball and forced you into a fight.")
    elif throw_ball == "1" and scyther_HP < 50:
        print("You successfully caught the scyther")
        return "Caught"
    elif throw_ball == "2":
        print("-"*100)
    elif throw_ball == "3":
        print("You successfully fled the scyther.")
        return "Fled"
    
    if starter_pokemon == "Fuecoco":
        print("1 = Tackle | 2 = Ember | 3 = Leer")
    elif starter_pokemon == "Sprigatito":
        print("1 = Leafage | 2 = Scratch | 3 = Tail Whip")
    elif starter_pokemon == "Quaxly":
        print("1 = Pound | 2 = Water Gun | 3 = Growl")

    move2 = input("What move would you like to use? ")
    if starter_pokemon == "Fuecoco" and move2 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move2 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        scyther_HP -= 30
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move2 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move2 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 15
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move2 == "2" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move2 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move2 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move2 == "2" and opponent_defense_lower == 0:
        print("It's Not Very Effective.")
        scyther_HP -= 8
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move2 == "3" and opponent_attack_lower == 0:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 1

    if starter_pokemon == "Fuecoco" and move2 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move2 == "2" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        scyther_HP -= 40
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move2 == "3" and opponent_defense_lower == 1:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Sprigatito" and move2 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 20
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move2 == "2" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move2 == "3" and opponent_defense_lower == 1:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Quaxly" and move2 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move2 == "2" and opponent_defense_lower == 1:
        print("It's Not Very Effective.")
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move2 == "3" and opponent_attack_lower == 1:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 2

    print("-"*100)

    if scyther_HP > 0 and opponent_attack_lower == 0:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 7
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 1:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 5
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 2:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 3
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)

    print("-"*100)

    if scyther_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {scyther_HP*-100} + {score}")

        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {scyther_HP*0.1+{score}}")
        return "Lost"
    
    throw_ball2 = input("What do you want to do? (1 for Throw Pokeball, 2 for Fight, 3 for Flee)")
    if throw_ball2 == "1" and scyther_HP == 50:
        print("The scyther escaped the ball and forced you into a fight.")
    elif throw_ball2 == "1" and scyther_HP < 50:
        print("You successfully caught the scyther")
        return "Caught"
    elif throw_ball2 == "2":
        print("-"*100)
    elif throw_ball2 == "3":
        print("You successfully fled the scyther.")
        return "Fled"
    
    if starter_pokemon == "Fuecoco":
        print("1 = Tackle | 2 = Ember | 3 = Leer")
    elif starter_pokemon == "Sprigatito":
        print("1 = Leafage | 2 = Scratch | 3 = Tail Whip")
    elif starter_pokemon == "Quaxly":
        print("1 = Pound | 2 = Water Gun | 3 = Growl")

    move3 = input("What move would you like to use? ")
    if starter_pokemon == "Fuecoco" and move3 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        scyther_HP -= 30
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move3 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 15
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "2" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move3 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "2" and opponent_defense_lower == 0:
        print("It's Not Very Effective.")
        scyther_HP -= 8
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "3" and opponent_attack_lower == 0:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 1

    if starter_pokemon == "Fuecoco" and move3 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "2" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        scyther_HP -= 40
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "3" and opponent_defense_lower == 1:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Sprigatito" and move3 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 20
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "2" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "3" and opponent_defense_lower == 1:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Quaxly" and move3 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "2" and opponent_defense_lower == 1:
        print("It's Not Very Effective.")
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "3" and opponent_attack_lower == 1:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 2

    if starter_pokemon == "Fuecoco" and move3 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "2" and opponent_defense_lower == 2:
        print("It's Super Effective!")
        scyther_HP -= 70
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move3 == "3" and opponent_defense_lower == 2:
        print("The opponents is at the lowest value possible")
    elif starter_pokemon == "Sprigatito" and move3 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "2" and opponent_defense_lower == 2:
        scyther_HP -= 35
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move3 == "3" and opponent_defense_lower == 2:
        print("The opponents defense is at the lowest value possible.")
    elif starter_pokemon == "Quaxly" and move3 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "2" and opponent_defense_lower == 2:
        print("It's Not Very Effective.")
        scyther_HP -= 25
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move3 == "3" and opponent_attack_lower == 2:
        print("The opponents attack is the lowest it can be.")

    print("-"*100)

    if scyther_HP > 0 and opponent_attack_lower == 0:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 7
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 1:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 5
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 2:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 3
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)

    print("-"*100)

    if scyther_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {scyther_HP*-100} + {score}")

        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {scyther_HP*0.1+{score}}")
        return "Lost"

    throw_ball = input("What do you want to do? (1 for Throw Pokeball, 2 for Fight, 3 for Flee)")
    if throw_ball == "1" and scyther_HP == 50:
        print("The scyther escaped the ball and forced you into a fight.")
    elif throw_ball == "1" and scyther_HP < 50:
        print("You successfully caught the scyther")
        return "Caught"
    elif throw_ball == "2":
        print("-"*100)
    elif throw_ball == "3":
        print("You successfully fled the scyther.")
        return "Fled"
    
    if starter_pokemon == "Fuecoco":
        print("1 = Tackle | 2 = Ember | 3 = Leer")
    elif starter_pokemon == "Sprigatito":
        print("1 = Leafage | 2 = Scratch | 3 = Tail Whip")
    elif starter_pokemon == "Quaxly":
        print("1 = Pound | 2 = Water Gun | 3 = Growl")

    move4 = input("What move would you like to use? ")
    if starter_pokemon == "Fuecoco" and move4 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        scyther_HP -= 30
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move4 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 15
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "2" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move4 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "2" and opponent_defense_lower == 0:
        print("It's Not Very Effective.")
        scyther_HP -= 8
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "3" and opponent_attack_lower == 0:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 1

    if starter_pokemon == "Fuecoco" and move4 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "2" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        scyther_HP -= 40
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "3" and opponent_defense_lower == 1:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Sprigatito" and move4 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 20
        print(f"Scythr HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "2" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "3" and opponent_defense_lower == 1:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Quaxly" and move4 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "2" and opponent_defense_lower == 1:
        print("It's Not Very Effective.")
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "3" and opponent_attack_lower == 1:
        print("The Growl lowered the opponents attack!")
        opponent_attack_lower = 2

    elif starter_pokemon == "Fuecoco" and move4 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "2" and opponent_defense_lower == 2:
        print("It's Super Effective!")
        scyther_HP -= 70
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move4 == "3" and opponent_defense_lower == 2:
        print("The opponents is at the lowest value possible")
    elif starter_pokemon == "Sprigatito" and move4 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "2" and opponent_defense_lower == 2:
        scyther_HP -= 35
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move4 == "3" and opponent_defense_lower == 2:
        print("The opponents defense is at the lowest value possible.")
    elif starter_pokemon == "Quaxly" and move4 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "2" and opponent_defense_lower == 2:
        print("It's Not Very Effective.")
        scyther_HP -= 25
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move4 == "3" and opponent_attack_lower == 2:
        print("The opponents attack is the lowest it can be.")

    print("-"*100)

    if scyther_HP > 0 and opponent_attack_lower == 0:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 7
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 1:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 5
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 2:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 3
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)

    print("-"*100)

    if scyther_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {scyther_HP*-100} + {score}")

        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {scyther_HP*0.1+{score}}")
        return "Lost"
    
    throw_ball = input("What do you want to do? (1 for Throw Pokeball, 2 for Fight, 3 for Flee)")
    if throw_ball == "1" and scyther_HP == 50:
        print("The scyther escaped the ball and forced you into a fight.")
    elif throw_ball == "1" and scyther_HP < 50:
        print("You successfully caught the scyther")
        return "Caught"
    elif throw_ball == "2":
        print("-"*100)
    elif throw_ball == "3":
        print("You successfully fled the scyther.")
        return "Fled"

    if starter_pokemon == "Fuecoco":
        print("1 = Tackle | 2 = Ember | 3 = Leer")
    elif starter_pokemon == "Sprigatito":
        print("1 = Leafage | 2 = Scratch | 3 = Tail Whip")
    elif starter_pokemon == "Quaxly":
        print("1 = Pound | 2 = Water Gun | 3 = Growl")

    move5 = input("What move would you like to use? ")
    if starter_pokemon == "Fuecoco" and move5 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move5 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        scyther_HP -= 30
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move5 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move5 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 15
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move5 == "2" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move5 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move5 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move5 == "2" and opponent_defense_lower == 0:
        print("It's Not Very Effective.")
        scyther_HP -= 8
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move5 == "3":
        print("The Growl lowered the opponents attack!")

    if starter_pokemon == "Fuecoco" and move5 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move5 == "2" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        scyther_HP -= 40
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move5 == "3" and opponent_defense_lower == 1:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Sprigatito" and move5 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 20
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move5 == "2" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move5 == "3" and opponent_defense_lower == 1:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Quaxly" and move5 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move5 == "2" and opponent_defense_lower == 1:
        print("It's Not Very Effective.")
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move5 == "3":
        print("The Growl lowered the opponents attack!")

    if starter_pokemon == "Fuecoco" and move5 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move5 == "2" and opponent_defense_lower == 2:
        print("It's Super Effective!")
        scyther_HP -= 70
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move5 == "3" and opponent_defense_lower == 2:
        print("The opponents is at the lowest value possible")
    elif starter_pokemon == "Sprigatito" and move5 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move5 == "2" and opponent_defense_lower == 2:
        scyther_HP -= 35
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move5 == "3" and opponent_defense_lower == 2:
        print("The opponents defense is at the lowest value possible.")
    elif starter_pokemon == "Quaxly" and move5 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move5 == "2" and opponent_defense_lower == 2:
        print("It's Not Very Effective.")
        scyther_HP -= 25
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move5 == "3":
        print("The Growl lowered the opponents attack!")

    print("-"*100)

    if scyther_HP > 0 and opponent_attack_lower == 0:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 7
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 1:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 5
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 2:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 3
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)

    print("-"*100)

    if scyther_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {scyther_HP*-100} + {score}")

        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {scyther_HP*0.1+{score}}")
        return "Lost"
    
    throw_ball2 = input("What do you want to do? (1 for Throw Pokeball, 2 for Fight, 3 for Flee)")
    if throw_ball2 == "1" and scyther_HP == 50:
        print("The scyther escaped the ball and forced you into a fight.")
    elif throw_ball2 == "1" and scyther_HP < 50:
        print("You successfully caught the scyther")
        return "Caught"
    elif throw_ball2 == "2":
        print("-"*100)
    elif throw_ball2 == "3":
        print("You successfully fled the scyther.")
        return "Fled"
    
    if starter_pokemon == "Fuecoco":
        print("1 = Tackle | 2 = Ember | 3 = Leer")
    elif starter_pokemon == "Sprigatito":
        print("1 = Leafage | 2 = Scratch | 3 = Tail Whip")
    elif starter_pokemon == "Quaxly":
        print("1 = Pound | 2 = Water Gun | 3 = Growl")

    move6 = input("What move would you like to use? ")
    if starter_pokemon == "Fuecoco" and move6 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move6 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        scyther_HP -= 30
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move6 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move6 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 15
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move6 == "2" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move6 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move6 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move6 == "2" and opponent_defense_lower == 0:
        print("It's Not Very Effective.")
        scyther_HP -= 8
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move6 == "3":
        print("The Growl lowered the opponents attack!")

    if starter_pokemon == "Fuecoco" and move6 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move6 == "2" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        scyther_HP -= 40
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move6 == "3" and opponent_defense_lower == 1:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Sprigatito" and move6 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 20
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move6 == "2" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move6 == "3" and opponent_defense_lower == 1:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Quaxly" and move6 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move6 == "2" and opponent_defense_lower == 1:
        print("It's Not Very Effective.")
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move6 == "3":
        print("The Growl lowered the opponents attack!")

    if starter_pokemon == "Fuecoco" and move6 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move6 == "2" and opponent_defense_lower == 2:
        print("It's Super Effective!")
        scyther_HP -= 70
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move6 == "3" and opponent_defense_lower == 2:
        print("The opponents is at the lowest value possible")
    elif starter_pokemon == "Sprigatito" and move6 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move6 == "2" and opponent_defense_lower == 2:
        scyther_HP -= 35
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move6 == "3" and opponent_defense_lower == 2:
        print("The opponents defense is at the lowest value possible.")
    elif starter_pokemon == "Quaxly" and move6 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move6 == "2" and opponent_defense_lower == 2:
        print("It's Not Very Effective.")
        scyther_HP -= 25
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move6 == "3":
        print("The Growl lowered the opponents attack!")

    print("-"*100)

    if scyther_HP > 0 and opponent_attack_lower == 0:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 7
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 1:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 5
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 2:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 3
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)

    print("-"*100)

    if scyther_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {scyther_HP*-100} + {score}")

        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {scyther_HP*0.1+{score}}")
        return "Lost"

    throw_ball2 = input("What do you want to do? (1 for Throw Pokeball, 2 for Fight, 3 for Flee)")
    if throw_ball2 == "1" and scyther_HP == 50:
        print("The scyther escaped the ball and forced you into a fight.")
    elif throw_ball2 == "1" and scyther_HP < 50:
        print("You successfully caught the scyther")
        return "Caught"
    elif throw_ball2 == "2":
        print("-"*100)
    elif throw_ball2 == "3":
        print("You successfully fled the scyther.")
        return "Fled"
    
    if starter_pokemon == "Fuecoco":
        print("1 = Tackle | 2 = Ember | 3 = Leer")
    elif starter_pokemon == "Sprigatito":
        print("1 = Leafage | 2 = Scratch | 3 = Tail Whip")
    elif starter_pokemon == "Quaxly":
        print("1 = Pound | 2 = Water Gun | 3 = Growl")

    move7 = input("What move would you like to use? ")
    if starter_pokemon == "Fuecoco" and move7 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move7 == "2" and opponent_defense_lower == 0:
        print("It's Super Effective!")
        scyther_HP -= 30
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move7 == "3" and opponent_defense_lower == 0:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Sprigatito" and move7 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 15
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move7 == "2" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move7 == "3" and opponent_defense_lower == 0:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 1
    elif starter_pokemon == "Quaxly" and move7 == "1" and opponent_defense_lower == 0:
        scyther_HP -= 12
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move7 == "2" and opponent_defense_lower == 0:
        print("It's Not Very Effective.")
        scyther_HP -= 8
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move7 == "3":
        print("The Growl lowered the opponents attack!")

    if starter_pokemon == "Fuecoco" and move7 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move7 == "2" and opponent_defense_lower == 1:
        print("It's Super Effective!")
        scyther_HP -= 40
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move7 == "3" and opponent_defense_lower == 1:
        print("The Leer lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Sprigatito" and move7 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 20
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move7 == "2" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move7 == "3" and opponent_defense_lower == 1:
        print("The Tail Whip lowered the opponents defense!")
        opponent_defense_lower = 2
    elif starter_pokemon == "Quaxly" and move7 == "1" and opponent_defense_lower == 1:
        scyther_HP -= 17
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move7 == "2" and opponent_defense_lower == 1:
        print("It's Not Very Effective.")
        scyther_HP -= 12
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move7 == "3":
        print("The Growl lowered the opponents attack!")

    if starter_pokemon == "Fuecoco" and move7 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move7 == "2" and opponent_defense_lower == 2:
        print("It's Super Effective!")
        scyther_HP -= 70
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Fuecoco" and move7 == "3" and opponent_defense_lower == 2:
        print("The opponents is at the lowest value possible")
    elif starter_pokemon == "Sprigatito" and move7 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move7 == "2" and opponent_defense_lower == 2:
        scyther_HP -= 35
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Sprigatito" and move7 == "3" and opponent_defense_lower == 2:
        print("The opponents defense is at the lowest value possible.")
    elif starter_pokemon == "Quaxly" and move7 == "1" and opponent_defense_lower == 2:
        scyther_HP -= 25
        print(f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move7 == "2" and opponent_defense_lower == 2:
        print("It's Not Very Effective.")
        scyther_HP -= 25
        print (f"Scyther HP: {scyther_HP}")
    elif starter_pokemon == "Quaxly" and move7 == "3":
        print("The Growl lowered the opponents attack!")

    print("-"*100)

    if scyther_HP > 0 and opponent_attack_lower == 0:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 7
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 1:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 5
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)
    elif scyther_HP > 0 and opponent_attack_lower == 2:
        print(f"Scyther used Quick Attack")
        l1_starter_pokemon_HP -= 3
        print(starter_pokemon, "HP:", l1_starter_pokemon_HP)

    print("-"*100)

    if scyther_HP <= 0:
        print("-"*100)
        print("The battle has ended.")
        print("YOU WIN!")
        print(f"{starter_pokemon} leveled up to level 2")
        print(f"You earned 100 Pokedollars")
        print(f"Final Score: {scyther_HP*-100} + {score}")

        return "Won"
    elif l1_starter_pokemon_HP <= 0:
        print("-"*100)
        print("The battle has ended")
        print("You Lose...")
        print("You earned 10 Pokedollars")
        print(f"Final Score: {scyther_HP*0.1+{score}}")
        return "Lost"
    
    print("-"*100)

if encounter == "1":
    rival_battle(starter_pokemon)
elif encounter == "2":
    scyther_encounter(starter_pokemon)