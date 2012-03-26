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

def remove_letter(original_string, letter):
    """
    original_string (string)
    letter (string): is of length 1

    Returns the original string with the first instance of the letter removed
    """
    assert type(original_string) == str
    assert type(letter) == str
    assert len(letter) == 1
    
    return original_string.partition(letter)[0] + original_string.partition(letter)[2]

def mask_letters(original_string, letters, mask_char):
    """
    original_string (string)
    letters (string)
    mask_char (string): is of length 1

    Returns the original string with any instance of the letters masked
    """
    assert type(original_string) == str
    assert type(letters) == str
    assert type(mask_char) == str
    assert len(mask_char) == 1
    
    for letter in letters:
        original_string = original_string.replace(letter, mask_char)
    return original_string

# Initialization of global variables
    
word = choose_word(wordlist)
available_letters = string.lowercase #'abcdefghijklmnopqrstuvwxyz'

# Main program body

print 'Welcome to the game, Hangman!'
print 'I am thinking of a word that is ' + str(len(word)) + ' letters long.'
print 'Pssssst.... The word is ' + word + ', ok?'
print '-----------------'

for guess in range(2, 0, -1):
    print 'You have ' + str(guess) + ' guesses left.'
    print 'Available letters: ' + available_letters
    letter = raw_input('Please guess a letter: ').lower()
    available_letters = remove_letter(available_letters, letter)
    if letter in word:
        print 'Good guess! ' + mask_letters(word, available_letters, '_')
    else:
        print 'Oops! That letter is not in my word. '
