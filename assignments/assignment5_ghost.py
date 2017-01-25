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


def is_valid_word(word, word_list):
    """Returns True if `word` is a valid word in `word_list`, False otherwise"""
    word_ls = get_valid_words()

    for letter in word_ls:
        if letter[:len(word)] == word:
            return True


def next_player(player):
    return 2 if player == 1 else 1


def ghost():
    """Start Ghost game"""
    word_list = load_words()
    current_word_fragment = ''
    current_player = 1
    print("Welcome to Ghost!")
    print("Player {} goes first." .format(current_player))

    while True:
        if current_word_fragment == '':
            print("Current word fragment: '{}'" .format(current_word_fragment))

            word = input("Player {} says letter: " .format(current_player)).lower()

            if word in string.ascii_letters and len(word) == 1:
                current_word_fragment += str(word)
                current_player = next_player(current_player)
            else:
                print("Invalid letter! word should be one letter and string")
                print("Please try again")
        else:
            if len(current_word_fragment) < 3:
                print("Current word fragment: '{}'" .format(current_word_fragment))
                print("Player {}'s turn." .format(current_player))

                word = input("Player {} says letter: " .format(current_player)).lower()

                if word in string.ascii_letters and len(word) == 1:
                    current_word_fragment += str(word)

                    current_player = next_player(current_player)
                else:
                    print("Invalid letter! word should be one letter and string")
                    print("Please try again")
            else:
                print("Current word fragment: '{}'" .format(current_word_fragment))

                if current_word_fragment in get_valid_words():
                    current_player = next_player(current_player)

                    print("Player {} loses because '{}' is a word"
                          .format(current_player, current_word_fragment))

                    current_player = next_player(current_player)

                    print("Player {} wins!" .format(current_player))
                    return

                if is_valid_word(current_word_fragment, get_valid_words()):
                    print("Player {}'s turn." .format(current_player))

                    word = input("Player {} says letter: " .format(current_player)).lower()

                    if word in string.ascii_letters and len(word) == 1:
                        current_word_fragment += str(word)

                        current_player = next_player(current_player)
                    else:
                        print("Invalid letter! word should be one letter and string")
                        print("Please try again")
                else:
                    current_player = next_player(current_player)

                    print("Player {} loses because no word begins with '{}'!"
                          .format(current_player, current_word_fragment))

                    current_player = next_player(current_player)

                    print("Player {} wins!" .format(current_player))

                    return

if __name__ == '__main__':
    ghost()
