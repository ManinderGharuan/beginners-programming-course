from assignment5 import get_valid_words, get_word_score, update_hand, is_valid_word


def test_get_word_score():
    word1, n1, ans1 = 'superman', 7, 62
    word2, n2, ans2 = 'it', 7, 2
    word3, n3, ans3 = 'scored', 7, 9
    word4, n4, ans4 = 'outgnaw', 7, 61
    word5, n5, ans5 = 'outgnawn', 8, 62

    assert get_word_score(word1, n1) == ans1
    assert get_word_score(word2, n2) == ans2
    assert get_word_score(word3, n3) == ans3
    assert get_word_score(word4, n4) == ans4
    assert get_word_score(word5, n5) == ans5


def test_update_hand():
    hand1 = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    word1 = "quail"
    #expected_hand1 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    expected_hand1 = {'l':1, 'm':1}

    hand2 = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word2 = "evil"
    #expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    expected_hand2 = {'v':1, 'n':1, 'l':1}

    hand3 = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    word3 = "hello"
    #expected_hand3 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    expected_hand3 = {}

    hand4 = {'a': 2, 'd': 1, 'e': 2, 'i': 1, 'm': 2, 'n': 4, 'r': 1}
    word4 = "maninder"
    #expected_hand4 = {'a': 1, 'd': 0, 'e': 1, 'i': 0, 'm': 1, 'n': 2, 'r': 0}
    expected_hand4 = {'a': 1, 'e': 1, 'm': 1, 'n': 2}

    hand5 = {'a': 1, 'c': 1, 'i': 1, 'h': 1, 'm': 2, 'z':1}
    word5 = ""
    expected_hand5 = {'a': 1, 'c': 1, 'i': 1, 'h': 1, 'm': 2, 'z':1}

    assert update_hand(hand1, word1) == expected_hand1
    assert update_hand(hand2, word2) == expected_hand2
    assert update_hand(hand3, word3) == expected_hand3
    assert update_hand(hand4, word4) == expected_hand4
    assert update_hand(hand5, word5) == expected_hand5


def test_is_valid_word():
    word_list = get_valid_words()

    word1 = 'hello'
    hand1 = {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    word2 = "rapture"
    hand2 = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}

    word3 = "honey"
    hand3 = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}

    word4 = "honey"
    hand4 = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}

    word5 = "evil"
    hand5 = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}

    assert is_valid_word(word1, hand1, word_list) is True
    assert is_valid_word(word2, hand2, word_list) is False
    assert is_valid_word(word3, hand3, word_list) is True
    assert is_valid_word(word4, hand4, word_list) is False
    assert is_valid_word(word5, hand5, word_list) is True
