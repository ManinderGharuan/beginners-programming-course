import time
import random

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


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}

    for x in sequence:
        freq[x] = freq.get(x, 0) + 1

    return freq


def get_word_total_score(word):
    """Returns total score of given ~word~"""
    score = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10,
        'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    total_score = 0

    for a_word in word:
        total_score += score.get(a_word)

    return total_score


def get_word_score(word, n):
    """Returns scores of ~word~ if ~word~ is valid"""
    scores = 0

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
    hand = {}
    num_vowels = int(n / 3)

    for i in range(num_vowels):
        x = VOWELS[random.randrange(len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


def update_hand(hand, word):
    """Returns the remaining dictionary of ~hand~ with removing ~word~"""
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
            return

    if valid_word and valid_hand:
        return True

    return False


def get_words_to_points(word_list):
    """Returns dictionary of word in ~word_list~ to its point value"""
    points_dict = {}

    for i in word_list:
        points_dict[i] = get_word_score(i, HAND_SIZE)

    return points_dict


def is_hand_in_dict(str_hand, key):
    check_str = key

    for i in str_hand:
        if check_str.find(i) >= 0:
            check_str = check_str.replace(i, '', 1)

    if check_str != '':
        return False
    else:
        return True


def pick_best_word(hand, points_dict):
    """
    Returns highest scoring word from ~points_dict~
    that can be made with given ~hand~
    """
    str_hand = display_hand(hand)
    best_words = {}

    for key in points_dict.keys():
        if is_hand_in_dict(str_hand, key):
            best_words[key] = points_dict.get(key)

    if best_words == {}:
        return '.'

    return max(best_words)


def get_words_rearrangement(word_list):
    rearrange_dict = {}

    for i in word_list:
        rearrange_dict[''.join(sorted(i))] = i

    return rearrange_dict


def pick_best_word_faster(hand, rearrange_dict):
    """Returns highest scorring word faster than ~pick_best_word~"""
    str_hand = display_hand(hand)
    best_words = {}

    for key in rearrange_dict.keys():
        if is_hand_in_dict(str_hand, key):
            best_words[rearrange_dict.get(key)] = get_word_score(key,
                                                                 HAND_SIZE)

    if best_words == {}:
        return '.'

    return max(best_words)


def get_time_limit(points_dict, k):
    """
    Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)

    end_time = time.time()

    return (end_time - start_time) * k


def play_hand(hand, word_list):
    """Allows the user to play the given hand"""
    points = 0
    new_hand = hand.copy()

    print("Enter time limit, in seconds, for players: {}"
          .format(comp_time_limit))

    time_limit = float(comp_time_limit)

    while True:
        current_hand = display_hand(new_hand)

        print("Current Hand: ", current_hand)

        start_time = time.time()

        print("Enter word, or . to indicate that you are finished: {}"
              .format(pick_best_word_faster(new_hand, rearrange_dict)))

        word = pick_best_word_faster(new_hand, rearrange_dict)

        end_time = time.time()
        total_time = end_time - start_time
        remaining_time = time_limit - total_time

        print("It tooks {} seconds to provide an answer." .format(total_time))
        print("You have {} secondss remaining." .format(remaining_time))

        if word == ".":
            print("Total score: ", points, " points.")
            break

        if remaining_time <= 0:
            print("Your Time is over, earned 0 score")
            print("Total score:  ", points, " points")
            return

        if is_valid_word(word, new_hand, word_list):
            score = get_word_score(word, HAND_SIZE)
            points += score

            print(word, " earned ", score, " points. Total: ",
                  points, " points")

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


if __name__ == "__main__":
    hand = deal_hand(HAND_SIZE)
    word_list = get_valid_words()
    points_dict = get_words_to_points(get_valid_words())
    comp_time_limit = get_time_limit(points_dict, 1.6)
    rearrange_dict = get_words_rearrangement(word_list)

    play_hand(hand, word_list)
