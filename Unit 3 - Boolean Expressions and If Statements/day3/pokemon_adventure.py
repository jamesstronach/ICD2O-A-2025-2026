def choose_pokemon():
    print("1 = Sprigatito, 2 = Fuecoco, 3 = Quaxly")
    pokemon_starters = (input("Enter the number of your pokemon: "))
    if pokemon_starters == "1":
        pokemon_starters = "Sprigatito"
    elif pokemon_starters == "2":
        pokemon_starters = "Fuecoco"
    elif pokemon_starters == "3":
        pokemon_starters = "Quaxly"

    return pokemon_starters 
pokemon = choose_pokemon()
print("You chose", pokemon)
def game_intro(pokemon):
    if pokemon == "Sprigatito":
        return f"{pokemon}, is a grass type pokemon and is a quadrupedal feline Pokémon covered in pale green fur. The fur's composition is similar to that of plants, allowing it to absorb sunlight for energy. It has green ears with pale green insides, a tuft of fur on the front of its chest and a green marking around its pink eyes and nose that resemble leaves. When its mouth is open, two pointed teeth can be seen in its upper jaw. It has a fluffy tail and small paws with pink paw pads underneath and no visible toes. Eventually, this little feline friend will join the darkside and take on a far stronger role"
    elif pokemon == "Fuecoco":
        return f"{pokemon}, is a fire pokemon that came from the woods. After he was born, he was the most playful and cheerful pokemon known to the school that hosts the disastrous, TEAM STAR. One day, he'll become a crocodile that will destroy everything in its path with his amazing singing voice."
    else:
        return f"{pokemon}, Quaxly is a water type pokemon and is a white duckling-like Pokémon. It has a yellow beak and blue eyes. It has teal webbed feet and a large teal coif-like crest that covers its head, with a feathery tuft in the front and a white curvy line shaped like a wave. Quaxly's coif has a smooth feel thanks to the rich, moist cream that holds it. The cream it secretes can repel grime. The coif can become unkempt should it get dry."
print(game_intro(pokemon))
