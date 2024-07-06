from file_ops import load_fruit
from fruits import picker_random as pick
from logicscripts.letter_numbers import count_char as letNum
from logicscripts.guesser import guess_Word as guessWord

FILE_PATH = './data/fruits.json'


def main():
    fruits = load_fruit(FILE_PATH) # load the jason db

    if not fruits:
        print("No Words Found")  
        return    
    
    while True:
        # Welcome Message
        print("\n Hi and welcome to Hangman, you will select a letter and ultimately strive to guess the word. You will have 5 chances to guess letters, and only one chance to guess the word. Good Luck!")
        # User UI
        print("\n 1 New Game")
        print("\n 2 Exit")        
        choice = input("\nPlease select an appopriate choice (1 or 2)")

        if choice == '1':
            # CODE THE GAME!
            word = pick().lower() # imports picker random from fruits.py and converts to lower
            length = letNum(word) # imports count_char from letters_numbers.py    
            life = 5 # initialises lives
            guessed_word = ['-'] * len(word) # calculates length of picked word and adds '-' character to the guess output
            make_a_guess = guessWord # imports guessword function from guesser.py !!!!!!!!!!!!!!!!!!!!!!

            print(f"\n The number of letters in your word are {length}")
            print("\n Please select a letter (a-z) or guess the word")
            
            while life >= 1: # set lives based on life to countdown
                print(word)
                first_Guess = input("\n Enter your guess: ").lower()  # Prompt for new input, convert to lower string                
                if len(first_Guess) > 1 and first_Guess == word: # if user guesses word early, Mad kudos
                    make_a_guess (guessed_word, word, first_Guess) # takes guesser.py logic and adds other initilisations as specific arguments
                    print(f"Wow, didn't expect you to guess {word} so easily! You brainiac you!")
                    break
                elif len(first_Guess) > 1 and first_Guess != word: # checks to see if input is a char(acceptable), or word (BREAK)
                    make_a_guess (guessed_word, word, first_Guess) # takes guesser.py logic and adds other initilisations as specific arguments
                    print(f"You entered more than one letter! And you guessed WRONG. The word was: {word}")
                    break
                #FIX THIS CODE!
                elif first_Guess in word and len(first_Guess) == 1:
                    make_a_guess (guessed_word, word, first_Guess) # takes guesser.py logic and adds other initilisations as specific arguments
                    print(f"\n Correct Guess! Your word so far is {''.join(guessed_word)}, and you have {life} guesses remaining")
                #FIX THIS CODE!
                else:
                    life -= 1 # removes a life for incorrect char guess
                    print(f"\n Incorrect Guess! Your word so far is {''.join(guessed_word)}, and you have {life} guesses remaining")
                    
                    if life == 0: # Ends game when lives run out
                        print(f"You've run out of guesses! The word was: {word}")
                        return main ()
        # END GAME CODE!
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("\nPlease select an appropriate choice (1 or 2).")
    
   
if __name__ == "__main__":
    main()