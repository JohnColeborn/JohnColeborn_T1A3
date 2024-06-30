from file_ops import load_fruit
from fruit_ops import fruit_picker
from fruits import picker_random as pick
from packages import guess_number as guessNum, letter_numbers as letNum

FILE_PATH = './data/fruits.json'


def main():
    fruits = load_fruit(FILE_PATH)

    if not fruits:
        print("No Words Found")  
        return
    while True:
        # Welcome Message
        print("Hi and welcome to Hangman, you will select a letter and ultimately strive to guess the word. You will have 5 chances to guess letters, and only one chance to guess the word. Good Luck!")
        # User UI
        print("\n 1 New Game")
        print("\n 2 Exit")        
        choice = input("Please select an appopriate choice (1 or 2)")

        if choice == '1':
            # INSERT GAME CODE HERE
            None
            # END GAME CODE HERE              
        elif choice == '2':
            exit()
        else:
            print("Please select an appopriate choice (1 or 2)")
            return True         
   
if __name__ == "__main__":
    main()