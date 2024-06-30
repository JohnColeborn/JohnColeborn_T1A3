from file_ops import load_fruit
from fruits import picker_random as pick
from logicscripts.letter_numbers import count_char as letNum
from logicscripts.guesser import guess_Word as guessWord

FILE_PATH = './data/fruits.json'


def main():
    fruits = load_fruit(FILE_PATH)

    if not fruits:
        print("No Words Found")  
        return    

    # Welcome Message
    print("\n Hi and welcome to Hangman, you will select a letter and ultimately strive to guess the word. You will have 5 chances to guess letters, and only one chance to guess the word. Good Luck!")

    while True:
        # User UI
        print("\n 1 New Game")
        print("\n 2 Exit")        
        choice = input("\nPlease select an appopriate choice (1 or 2)")

        if choice == '1':
            # INSERT GAME CODE HERE          
            word = pick().lower()            
            length = letNum(word)        
            life = 5           
            guessed_word = ['-'] * len(word)
            make_a_guess = guessWord

            print(f"\n The number of letters in your word are {length}")
            print("\n Please select a letter (a-z) or guess the word")
            
            while life >= 0:
                firstGuess = input("\n Enter your guess: ").lower()  # Prompt the user for a new guess
                
                if firstGuess in word:
                    make_a_guess(guessed_word, word, firstGuess)
                    print(f"\nCorrect Guess! Your word so far is {''.join(guessed_word)}, and you have {life} guesses remaining")
                # break the loop if they guess a word... only one guess ok!
                elif ''.join(guessed_word) == word:
                    print(f"Congratulations! You've guessed the word: {word}")
                    break
                elif ''.join(guessed_word) != word and '':
                    print(f"What have you DONE! You've not guessed the word: {word}")
                    break
                else:
                    print(f"\nIncorrect Guess! Your word so far is {''.join(guessed_word)}, and you have {life} guesses remaining")
                
                life -= 1

                # END GAME CODE HERE              
        elif choice == '2':
            exit()
        else:
            print("\n Please select an appopriate choice (1 or 2)")
            return True         
   
if __name__ == "__main__":
    main()