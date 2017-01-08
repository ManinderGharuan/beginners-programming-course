from assignment2 import is_possible, max_impossible


def test_is_possible():
    assert is_possible(3) is False
    assert is_possible(69) is True
    assert is_possible(17, 5, 8, 10) is False
    assert is_possible(23, 5, 8, 10) is True
    assert is_possible(30, 4, 6, 30) is True
    assert is_possible(31, 4, 6, 30) is False


def test_max_impossible():
    assert max_impossible() == 43
    assert max_impossible(10, 15, 22) == 83
    assert max_impossible(20, 1, 30) == 19
    assert max_impossible(25, 15, 11) == 57
    assert max_impossible(21, 5, 15) == 79
