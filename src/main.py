from file_ops import load_fruit
from fruits import picker_random as pick
from logicscripts.letter_numbers import count_char as letNum
# from logicscripts.guesser import guess_Word as guessWord OBSOLETE LOGIC 

FILE_PATH = '../data/fruits.json'

def main():
    fruits = load_fruit(FILE_PATH)  # load the json db

    if not fruits:
        print("No Words Found")
        return

    while True:
        # Welcome Message
        print("\nHi and welcome to Hangman! \nYou will select a letter and ultimately strive to guess the word. \nYou will have 5 chances to guess letters, \nOnly one chance to guess the word. Good Luck!")
        # User UI
        print("\n1. New Game")
        print("\n2. Exit")
        choice = input("\nPlease select an appropriate choice (1 or 2): ")

        if choice == '1':
            # CODE THE GAME!
            word = pick().lower()  # imports picker_random from fruits.py and converts to lower
            length = letNum(word)  # imports count_char from letter_numbers.py
            life = 5  # initializes lives
            guessed_word = ['-'] * len(word)  # initializes guessed word with dashes
            # make_a_guess = guessWord # imports guessword function from guesser.py OBSOLETE LOGIC
            print(f"\nThe number of letters in your word are {length}")
            print("\nPlease select a letter (a-z) or guess the word")

            while life >= 1:  # set lives based on life to countdown
                guess = input("\nEnter your guess: ").lower()  # Prompt for new input, convert to lower string
                if len(guess) > 1: # IF WORD LOGIC
                    if guess == word:  # if user guesses word correctly
                        print(f"Wow, didn't expect you to guess {word} so easily! You brainiac you!")
                        break
                    else:  # if user guesses the word incorrectly
                        print(f"You entered more than one letter! And you guessed WRONG. The word was: {word}")
                        break
                elif guess in word:  # IF CHARACTER LOGIC ...
                    guessed_word = [guess if c == guess else gw for c, gw in zip(word, guessed_word)]  # Updates guessed word based on correct guess c for character gw for guessed word
                    if ''.join(guessed_word) == word:  # If word is guessed by char completion SUCCESS
                        print(f"Wow, didn't expect you to guess {word} so easily! You brainiac you!")
                        break
        # FIX THIS BLOCK - USING ENTER key prints as CORRECT when it should NOT
                    else:
                        if guess in word:                             
                            life -= 1  # removes a life for guess
                            print(f"\nCorrect Guess! Your word so far is {''.join(guessed_word)}, and you have {life} guesses remaining")
                        else:
                            break
        # FIX THIS BLOCK                            
                else:
                    life -= 1  # removes a life for guess
                    print(f"\nIncorrect Guess! Your word so far is {''.join(guessed_word)}, and you have {life} guesses remaining")
            else:  # End Game
                if life == 0:  # Ends game when lives run out
                    print(f"You've run out of guesses! The word was: {word}")
                    return main()
                   


        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("\nPlease select an appropriate choice (1 or 2).")

if __name__ == "__main__":
    main()
