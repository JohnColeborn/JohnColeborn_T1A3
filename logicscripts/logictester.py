# Initialize the word and the current guessed state
word = "apple"
guessed_word = ["-"] * len(word)
lives = 5

# Function to update the guessed word
def update_guessed_word(guessed_word, word, guess):
    for i, letter in enumerate(word):
        if letter == guess:
            guessed_word[i] = guess

# First guess
firstGuess = "p"

# Check if the first guess is in the word
if firstGuess in word:
    update_guessed_word(guessed_word, word, firstGuess)
    print(f"\nCorrect Guess! Your word so far is {''.join(guessed_word)}, and you have {lives} guesses remaining")
else:
    lives -= 1
    print(f"\nIncorrect Guess! Your word so far is {''.join(guessed_word)}, and you have {lives} guesses remaining")
