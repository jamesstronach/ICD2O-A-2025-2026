player = input("What is your name? ")
def choose_pokemon():
    print("1 = Sprigatito, 2 = Fuecoco, 3 = Quaxly")
    pokemon_starters = (input("Enter the number of your pokemon: "))
    if pokemon_starters == "1":
        pokemon_starters = "Sprigatito"
    elif pokemon_starters == "2":
        pokemon_starters = "Fuecoco"
    else:
        pokemon_starters = "Quaxly"

    return pokemon_starters 
starter_pokemon = choose_pokemon()
print("You chose", starter_pokemon)
rival = input("What is your best friend/rivals name? ")
def choose_rival_starter_pokemon():
    if starter_pokemon == "Sprigatito":
        rival_starter_pokemon_choice = "Quaxly"
    elif starter_pokemon == "Fuecoco":
        rival_starter_pokemon_choice = "Sprigatito"
    elif starter_pokemon == "Quaxly":
        rival_starter_pokemon_choice == "Fuecoco"

        return rival_starter_pokemon_choice
rival_starter_pokemon = choose_rival_starter_pokemon()
def starter_pokemon_intro(starter_pokemon):
    if starter_pokemon == "Sprigatito":
        return f"{starter_pokemon}, is a grass type pokemon and is a quadrupedal feline Pokémon covered in pale green fur. The fur's composition is similar to that of plants, allowing it to absorb sunlight for energy. It has green ears with pale green insides, a tuft of fur on the front of its chest and a green marking around its pink eyes and nose that resemble leaves. When its mouth is open, two pointed teeth can be seen in its upper jaw. It has a fluffy tail and small paws with pink paw pads underneath and no visible toes. Eventually, this little feline friend will join the darkside and take on a far stronger role"
    elif starter_pokemon == "Fuecoco":
        return f"{starter_pokemon}, is a fire pokemon that came from the woods. After it was born, it was the most playful and cheerful pokemon known to the school that hosts the disastrous, TEAM STAR. One day, it will become a crocodile that will destroy everything in its path with its amazing singing voice."
    else:
        return f"{starter_pokemon}, Quaxly is a water type pokemon and is a white duckling-like Pokémon. It has a yellow beak and blue eyes. It has teal webbed feet and a large teal coif-like crest that covers its head, with a feathery tuft in the front and a white curvy line shaped like a wave. Quaxly's coif has a smooth feel thanks to the rich, moist cream that holds it. The cream it secretes can repel grime. The coif can become unkempt should it get dry."
print(starter_pokemon_intro(starter_pokemon))
def player_intro(player, starter_pokemon):
    print (f"Welcome to the world of pokemon, {player}. I'm sure you and your {starter_pokemon} will make a great team. You've just turned 10 years old, growing up in the middle of nowhere in the woods, and you're ready to explore the world, but not so fast. Your rival {rival} is trying to beat you and you need to prove you're better than him to fulfill your superiority complex." )
print(player_intro(player, starter_pokemon))
print(f"You start walking 2 kilometres away from your house, further than you've ever gone and you can see a city in the distance. Do you go to the city? Or walk another direction towards more wild and tall grass?")
walking_towards = input("Do you go to the city? Or walk another direction towards more wild and tall grass? (1 is city, 2 and others is grass)")
def make_decision():
    if walking_towards == "1":
        return "As you're walking towards the city, you encounter your best friend."
    elif walking_towards == "2":
        return "You walk towards the plains and encounter a wild scyther."
encounter = make_decision()
def first_battle():
    if encounter == "1":
        return f"Beginning battle with {rival}.\n{starter_pokemon} HP: 67\n{rival_starter_pokemon} HP: 40"
    elif encounter == "2":
        return f"test"
print(first_battle())
