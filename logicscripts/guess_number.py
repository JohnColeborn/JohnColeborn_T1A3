def guess_Num():
    # Initialise number of guesses
    guess = 5

    while guess >= 5:    
        numberGuessed = input()
        guess -= 1
        return numberGuessed