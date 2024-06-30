# Initialise number of guesses
guess = 0

while guess <= 0:
    print("You have five guesses remaining")
    firstGuess = input()
    guess += 1
print(firstGuess)