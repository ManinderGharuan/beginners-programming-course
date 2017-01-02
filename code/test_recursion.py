from recursion import (is_palindrome,
                       total,
                       fibonacci,
                       binary_search,
                       factorial,
                       length)


def test_length():
    assert length([]) == 0
    assert length([1]) == 1
    assert length([5, 3, 7, 2, 67, 4, 7, 4, 7]) == 9
    assert length([3, 6, 4, 2, 7, 55, 33, 77, 33, 5, 33]) == 11
    assert length([33, 77, 44]) == 3


def test_total():
    assert total([]) == 0
    assert total([4]) == 4
    assert total([3, 6, 1, 3]) == 13
    assert total([2, 6, 3, 8]) == 19
    assert total([9, 3, 6, 4, 8]) == 30


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(9) == 362880


def test_is_palindrome():
    assert is_palindrome('') is True
    assert is_palindrome('a') is True
    assert is_palindrome('abba') is True
    assert is_palindrome('abbab') is False
    assert is_palindrome('kanak') is True
    assert is_palindrome('123123') is False


def test_binary_search():
    assert binary_search(2, []) is False
    assert binary_search(2, [2]) is True
    assert binary_search(2, [5]) is False
    assert binary_search(8, [2, 3, 4, 5, 7]) is False
    assert binary_search(8, [2, 3, 4, 5, 7, 9]) is False
    assert binary_search(10, [1, 3, 5, 6, 8, 10, 44]) is True
    assert binary_search(4, [7, 6, 33, 55, 44, 77]) is False


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(4) == 3
    assert fibonacci(8) == 21
