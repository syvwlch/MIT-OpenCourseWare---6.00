# Problem set 3a
# Name: Mathieu Glachant
# Collaborators: None
# Time: Problem 6a: 0:20
#       Problem 6b: 0:15
#       Problem 6c: 0:15

from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    best_word = None
    best_score = 0
    print 'Computer looking for a good word'
    for number_letters in range(1, calculate_handlen(hand) + 1):
        #print 'Looking for words that are ', number_letters, ' letters long.'
        print '.',
        permutations = get_perms(hand, number_letters)
        for permutation in permutations:
            if permutation in word_list:
                score = get_word_score(permutation, HAND_SIZE)
                #print permutation, ' is a word, and it scores ', score, ' points.'
                if score > best_score:
                    #print permutation, 'is a word and it scores ', score, ' points.'
                    best_score = score
                    best_word = permutation
    return best_word

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    score = 0
    play_hand = hand.copy()
    while calculate_handlen(play_hand) > 0:
        print 'Current hand: ', display_hand(play_hand)
        word = comp_choose_word(hand, word_list)
        if word != None:
            word_score = get_word_score(word, HAND_SIZE)
            score += word_score
            hand = update_hand(play_hand, word)
            print '"', word, '" earned ',
            print word_score, ' points. ',
            print 'Total: ', score, ' points.'
        else:
            break
    print 'Total score: ', score, ' points.'
    return score  
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    print 'Starting the game with a new, random hand.'
    choice_nre = 'n'
    while True:
        choice_uc = ''
        while choice_uc not in ('u', 'c'):
            print 'Please choose from the following:'
            print '  "u" to play the hand yourself.'
            print '  "c" to let the computer play the hand.'
            choice_uc = raw_input('Choice: ').lower()
        if choice_nre == 'n':
            hand = deal_hand(HAND_SIZE)
        if choice_uc == 'u':
            play_hand(hand, word_list)
        else:
            comp_play_hand(hand, word_list)
        print
        choice_nre = ''
        while choice_nre not in ('e', 'n', 'r'):
            print 'Please choose from the following:'
            print '  "n" to play a new, random hand.'
            print '  "r" to play again with the same hand.'
            print '  "e" to exit the game.'
            choice_nre = raw_input('Choice: ').lower()
        if choice_nre == 'e':
            break
    return  None
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
