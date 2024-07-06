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
                first_Guess = input("\n Enter your guess: ").lower()  # Prompt for new input, convert to lower string                
                if len(first_Guess) > 1 and first_Guess == word: # if user guesses word early, Mad kudos
                    make_a_guess (guessed_word, word, first_Guess) # takes guesser.py logic and adds other initilisations as specific arguments
                    print(f"Wow, didn't expect you to guess {word} so easily! You brainiac you!")
                    break
                elif len(first_Guess) > 1 and first_Guess != word: # checks to see if input is a char(acceptable), or word (BREAK)
                    make_a_guess (guessed_word, word, first_Guess) # takes guesser.py logic and adds other initilisations as specific arguments
                    print(f"You entered more than one letter! And you guessed WRONG. The word was: {word}")
                    break
                elif first_Guess in word and len(first_Guess) == 1: # Correct Character Guess!!!
                    if guessed_word == word: # IF word is guessed by char completion (short words only), end game in SUCCESS 
                        print(f"Wow, didn't expect you to guess {word} so easily! You brainiac you!")
                    else:                        
                        life -= 1 # removes a life for guess
                        make_a_guess (guessed_word, word, first_Guess) # takes guesser.py logic and adds other initilisations as specific arguments                    
                        print(f"\n Correct Guess! Your word so far is {''.join(guessed_word)}, and you have {life} guesses remaining")
                        

                else:
                    life -= 1 # removes a life for guess
                    print(f"\n Incorrect Guess! Your word so far is {''.join(guessed_word)}, and you have {life} guesses remaining")
                    
#  # Ends game when lives run out                               IF CHAR IS CORRECT FIX HERE OR NOT FIX HERE
#                                             # Print word once life == 0
#                     if life == 0 and word == make_a_guess:
#                         print(f"Cracking Good Job for deducing: {word}")                              FIX THIS!!!!!!!!!!!!!
#                     elif life == 0 and word != make_a_guess:
#                         print(f"RIP, the word was: {word}")
#                     else:
#                         print(f"You've run out of guesses! The word was: {word}")
#                         return main ()                    # if life == 0:
        # END GAME CODE!
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("\nPlease select an appropriate choice (1 or 2).")
    
   
if __name__ == "__main__":
    main()