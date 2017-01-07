from assignment2 import is_possible, max_impossible


def test_is_possible():
    assert is_possible(3) is False
    assert is_possible(6) is True
    assert is_possible(7) is False
    assert is_possible(50) is True
    assert is_possible(61) is True


def test_max_impossible():
    assert max_impossible(50) == 43
    assert max_impossible(60) == 43
