# Initialise number of guesses
guess = 5

while guess >= 5:
    print("You have five guesses remaining")
    guessNum = input()
    guess -= 1
print(f"You chose: {guessNum}, You have {guess} attempts remaining")