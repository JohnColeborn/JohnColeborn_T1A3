# Hangman

A basic premise of word guessing, pick a letter, seven chances to guess the word based around 7 individual letter choices.

Create a premise.

# Premise

The words are limited to (Apple, Banana, Cacao, Durian, Elderberry, Fig, Grapefruit, Hazelnut, Icaco, Jackfruit, Kiwi, Lime, Mandarin, Nectarine)

Exciting fast-paced gameplay

More than 13 words to guess from

Play-by-play feedback - Feedback mechanisms
- Stunning victory messages
- Tragic losing messages

Tracking guesses - Limited attempts

Random word selection

    Will need to create alphabet to query from
    Will need to create Random.Range
    Will need to create Fruit Array


# Psuedocode

    Welcome Message:

    Hi and welcome to Hangman, you will select a letter and ultimately strive to guess the word. You will have 5 chances to guess letters, and only one chance to guess the word. Good Luck!

System Prompt

    Your word has (x) number of letters
    Please Select a letter of the alphabet to start (a-z)
Will use .lower on input

Any output outside a-z or a word will count as incorrect input and ask for correct input.

Any word (more than 1 letter simultaneously) will count as a word guess and initiate endgame

Correct Input received:

    You selected "x", this is not contained in your word, you have four guesses remaining

    or

    You selected "x", this is the (number position) letter of your (x numbered) word, you have four guesses remaining

Incorrect Input received:

    You have not entered a letter between a-z, please try again

Recur 5 times, unless word is guessed prior. Final guess:

    You selected "x", this is not contained in your word, you have no guesses remaining please guess a word

    or

    You selected "x", this is the (number position) letter of your (x numbered) word, you have no guesses remaining please guess a word

Correct Word:

    Congratulations, Your word was (randomWord)! You guessed correctly!

Incorrect Word: 

    Oh No!, Your word was (randomWord)! You guessed incorrectly!

Option to try again or exit:

    Would you like to try again (Y/N)
    if yes (restart)
    elif no
        would you like to exit? (Y/N)
        if yes(exit)
        elif no
            throw silly error for messing with time
    else roll credits

# Tools needed

- Random.Range
- Word Array
- Alphabet Array
- Packages (Fruits)(Letters)(Numbers)




# Start Coding 

- Create Character counter to check how many letters in each word
    - return to number count output (word has 7 letters to guess)
    - check for duplicate letters
        - return appropriate output (word has two of this letter)

- Create Fruit Word List and Random word picker
    - import random
    - Fruit name, length of word

- Create number of guess tracker
    - total number of guesses
    - input received = guess number
    - input remaining printed

- Create JSON for fruits

- Link Database, Operation modules, execute in Main











