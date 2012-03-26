# Problem Set 2
# Name: Mathieu Glachant
# Collaborators (Discussion): None
# Time: 


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

word = choose_word(wordlist)
    
print 'Welcome to the game, Hangman!'
print 'I am thinking of a word that is ' + str(len(word)) + ' letters long.'
print 'Pssssst.... It is ' + word
print '-----------------'

for guess in range(2, 0, -1):
    print 'You have ' + str(guess) + ' guesses left.'
    letter = raw_input('Please guess a letter: ')
    if letter in word:
        print 'Good guess!'
    else:
        print 'Oops! That letter is not in my word.'