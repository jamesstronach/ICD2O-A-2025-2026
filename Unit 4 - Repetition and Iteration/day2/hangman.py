import random
def display_word(hidden, guessed):
    display = ""
    for index in range(len(hidden)):
        letter = hidden[index]
        if letter in guessed:
            display += letter 
        else:
            display += "_"



    return display

def hangman():
    words = ["alphabet", "placeholder", "cellphone", "computer", "algorithm", "microsoft"]
    hidden = random.choice(words)

    maxGuess = 5
    gameover = False
    numguesses = 0
    guessedletters = "_"
    while(not gameover):
        print(display_word(hidden, guessedletters))
        guess = input("Choose a letter: ")
        if guess in guessedletters:
            print("Pick a different letter dipshit")
        elif len(guess)>1:
            print("nO")
        elif not (guess in hidden):
            print("nO")
            numguesses += 1
            guessedletters += guess
            if numguesses == maxGuess:
                print("DAYUM. YOU SUCK.")
                gameover = True
        else:
            guessedletters += guess
            if display_word(hidden,guessedletters) == hidden:
                print("W")
                gameover = True

hangman()




