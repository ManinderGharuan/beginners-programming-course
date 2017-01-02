def length(ls):
    """Return length of `ls`"""
    if ls == []:
        return 0

    return 1 + length(ls[1:])


def total(ls):
    """Return sum of all numbers inside `ls`"""
    if ls == []:
        return 0

    return ls[0] + total(ls[1:])


def factorial(num):
    """Return factorial of `num`"""
    if num <= 0:
        return 1

    return num * factorial(num - 1)


def is_palindrome(string):
    """Return True if given string is palindrome, False otherwise"""
    if string == '' or len(string) == 1:
        return True

    return string[0] == string[-1] and is_palindrome(string[1:-1])


def binary_search(num, ls):
    """Return True if `num` is in `ls`, False otherwise"""
    if ls == []:
        return False

    mid = len(ls)/2

    if ls[mid] == num:
        return True

    elif mid == 0:
        return False

    if ls[mid] < num:
        return binary_search(num, ls[mid:])

    else:
        return binary_search(num, ls[:mid])


def fibonacci(num):
    """Return `num`th number from Fibonacci series"""
    if num == 0:
        return 0

    elif num == 1:
        return 1

    return fibonacci(num-2) + fibonacci(num-1)
