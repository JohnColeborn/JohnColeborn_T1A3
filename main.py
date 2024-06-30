from file_ops import load_fruit
from fruits import picker_random as pick
from logicscripts.letter_numbers import count_char as letNum, count_unique_char as duplicateNum
from logicscripts.guesser import guess_Num, guess_Word as guessWord
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
        print("\n 1 Start Game")
        print("\n 2 Exit")        
        choice = input("\nPlease select an appopriate choice (1 or 2)")

        if choice == '1':
            # INSERT GAME CODE HERE          
            word = pick()            
            length = letNum(word)        
            lives = guess_Num            
            guessed_word = ['-'] * len(word)
            make_a_guess = guessWord
            print(f"\n The number of letters in your word are {length}")
            print("Please select a letter (a-z)")

            firstGuess = input().lower()
            # if first guess is a correct letter (p in the word apple), print correct guess 4 guess remaining - P P - - 
            if firstGuess in word:
                make_a_guess(guessed_word, word, firstGuess)
                lives -= 1
                print(f"\nCorrect Guess! Your word so far is {''.join(guessed_word)}, and you have {lives} guesses remaining")
            elif firstGuess not in word:                         
                print(f"\nIncorrect Guess! Your word so far is {''.join(guessed_word)}, and you have {lives} guesses remaining")
                return lives
            last_guess = lives 
            

            print(f"the word is {word}") # Visual confirmation of word working lol, PLX DELETE
            # END GAME CODE HERE              
        elif choice == '2':
            exit()
        else:
            print("\n Please select an appopriate choice (1 or 2)")
            return True         
   
if __name__ == "__main__":
    main()