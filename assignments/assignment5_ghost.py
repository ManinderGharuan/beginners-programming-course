from assignment5 import get_valid_words
import string


def load_words():
    """Returns a list of valid words. Words are strings of lowercase letters."""
    print("Loading word list from file...")
    wordlist = []

    with open('words.txt') as words_text:
        for word in words_text:
            wordlist.append(word.strip().lower())

    print("  ", len(wordlist), "words loaded.")

    return wordlist


def is_word_begins_valid(word, word_list):
    """Returns True if word is begins, False otherwise"""
    word_ls = get_valid_words()

    for letter in word_ls:
        if letter[:len(word)] == word:
            return True


def change_current_player(player):
    """Returns player number whose turn"""
    current_player = player

    if current_player == 1:
        current_player += 1
    else:
        current_player -= 1

    return current_player


def ghost():
    """Start Ghost game between two players"""
    word_list = load_words()
    current_word_fregment = ''
    current_player = 1
    print("Welcome to Ghost!")
    print("Player {} goes first." .format(current_player))

    while True:
        if current_word_fregment == '':
            print("Current word fregment: '{}'" .format(current_word_fregment))

            word = input("Player {} says letter: " .format(current_player)).lower()

            if word in string.ascii_letters and len(word) == 1:
                current_word_fregment += str(word)
                current_player = change_current_player(current_player)
            else:
                print("Invalid letter! word should be one letter and string")
                print("Please try again")
        else:
            if len(current_word_fregment) < 3:
                print("Current word fregment: '{}'" .format(current_word_fregment))
                print("Player {}'s turn." .format(current_player))

                word = input("Player {} says letter: " .format(current_player)).lower()

                if word in string.ascii_letters and len(word) == 1:
                    current_word_fregment += str(word)

                    current_player = change_current_player(current_player)
                else:
                    print("Invalid letter! word should be one letter and string")
                    print("Please try again")
            else:
                print("Current word fregment: '{}'" .format(current_word_fregment))

                if current_word_fregment in get_valid_words():
                    current_player = change_current_player(current_player)

                    print("Player {} loses because '{}' is a word"
                          .format(current_player, current_word_fregment))

                    current_player = change_current_player(current_player)

                    print("Player {} wins!" .format(current_player))
                    return

                if is_word_begins_valid(current_word_fregment, get_valid_words()):
                    print("Player {}'s turn." .format(current_player))

                    word = input("Player {} says letter: " .format(current_player)).lower()

                    if word in string.ascii_letters and len(word) == 1:
                        current_word_fregment += str(word)

                        current_player = change_current_player(current_player)
                    else:
                        print("Invalid letter! word should be one letter and string")
                        print("Please try again")

                else:
                    current_player = change_current_player(current_player)

                    print("Player {} loses because no word begins with '{}'!"
                          .format(current_player, current_word_fregment))

                    current_player = change_current_player(current_player)

                    print("Player {} wins!" .format(current_player))

                    return
