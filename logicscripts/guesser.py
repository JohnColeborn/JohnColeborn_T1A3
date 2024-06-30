def guess_Num():
    guess = 5  # Initialize the number of guesses allowed
    while guess > 0:    
        numberGuessed = input(f"You have {guess} guesses left. Please enter your guess: ")
        guess -= 1
        print(f"You guessed: {numberGuessed}")
    return numberGuessed
    
def guess_Word(guessed_word, word, guess):
    for i, letter in enumerate(word):
        if letter == guess:
            guessed_word[i] = guess

