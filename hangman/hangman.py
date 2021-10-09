# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def drawing(count):
    if count == 1:
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif count == 2:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif count == 3:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")

    elif count == 4:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")

    elif count == 5:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")


def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    return set(secretWord) <= set(lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    return ' '.join(x if x in (set(secretWord) & set(lettersGuessed)) else '_' for x in secretWord)


def getAvailableLetters(lettersGuessed):
    return ''.join(x if x not in lettersGuessed else '' for x in string.ascii_lowercase)

def hangman(secretWord):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []
    while mistakesMade < 5:
        print("-----------")
        print("You have", 5 - mistakesMade,  "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        letter =input("Please guess a letter: ")
        if letter.lower() in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(letter.lower())
            if letter.lower() in secretWord:
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print("-----------")
                    print("Congratulations, you won!")
                    break
            else:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                mistakesMade += 1
                drawing(mistakesMade)
    if mistakesMade == 5:
        print("-----------")
        print("Sorry, you ran out of guesses. The word was", secretWord, ".")


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
