import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7


def get_valid_words():
    """Returns list of valid words"""
    words = []

    with open('words.txt') as words_txt:
        for word in words_txt:
            words.append(word.strip().lower())

    return words


def get_word_total_score(word):
    """Returns total score of given ~word~"""
    score = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    total_score = 0

    for a_word in word:
        total_score += score.get(a_word)

    return total_score


def get_word_score(word, n):
    """Returns scores of ~word~ if ~word~ is valid"""
    scores = 0

    for valid_word in get_valid_words():
        if valid_word == word:
            if len(word) >= n:
                scores += 50

            scores += get_word_total_score(word)

    return scores


def display_hand(hand):
    """Displays the letters currently in the hand."""
    display_hand = ""

    for letter in hand.keys():
        for j in range(hand[letter]):
            display_hand += letter + " "

    return display_hand.strip()


def deal_hand(n):
    """Returns a random hand containing n lowercase letters.
       At least n/3 the letters in the hand should be VOWELS."""
    hand={}
    num_vowels = int(n / 3)

    for i in range(num_vowels):
        x = VOWELS[random.randrange(len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


def update_hand(hand, word):
    """Returns the remanining dictionary of ~hand~ with removing ~word~"""
    new_hand = hand.copy()

    for key in word.lower():
        new_hand[key] = new_hand.get(key) - 1

        if new_hand.get(key) == 0:
            new_hand.pop(key)

    return new_hand


def is_valid_word(word, hand, word_list):
    """Returns True if ~word~ is in the ~word_list~ and
       ~hand~ is having letters of ~word~, False otherwise"""
    temp_hand = hand.copy()
    valid_word = False
    valid_hand = False

    if word in word_list:
        valid_word = True

    for key in word:
        if key in temp_hand:
            if temp_hand.get(key) > 0:
                temp_hand[key] = temp_hand.get(key) - 1
                valid_hand = True

                if temp_hand.get(key) == 0:
                    temp_hand.pop(key)

        else:
            valid_hand = False
            break

    if valid_word and valid_hand:
        return True

    else:
        return False


def play_hand(hand, word_list):
    """Allows the user to play the given hand"""
    points = 0
    new_hand = hand.copy()

    while True:
        current_hand = display_hand(new_hand)

        print("Current Hand: ", current_hand)

        word = input("Enter word, or . to indicate that you are finished: ")

        if word == ".":
            print("Total score: ", points, " points.")
            return

        if is_valid_word(word, new_hand, word_list):
            score = get_word_score(word, HAND_SIZE)
            points += score

            print(word, " earned ", score, " points. Total: ", points, " points")
            new_hand = update_hand(new_hand, word)

        else:
            print("Invalid word, Please try again.")

        if new_hand == {}:
            print("Total score: ", points, " points.")
            return


def play_game(word_list):
    """Allow the user to play an arbitrary number of hands"""
    hand = deal_hand(HAND_SIZE)

    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print

        if cmd == 'r':
            play_hand(hand.copy(), word_list)
            print

        if cmd == 'e':
            return
        else:
            print("Invalid command.")
