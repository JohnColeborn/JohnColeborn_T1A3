from file_ops import load_fruit
from fruits import picker_random as pick
from packages.letter_numbers import count_char as letNum, count_unique_char as duplicateNum
from packages.guess_number import guess_Num as livesLeft
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
            print(f"The number of letters in your word are {length}")
            print(f"the word is {word}") # Visual confirmation of word working lol, PLX DELETE
            # END GAME CODE HERE              
        elif choice == '2':
            exit()
        else:
            print("\n Please select an appopriate choice (1 or 2)")
            return True         
   
if __name__ == "__main__":
    main()