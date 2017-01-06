from assignment1 import is_prime, get_primes


def test_is_prime():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(1778) is False
    assert is_prime(4481) is True


def test_get_primes():
    assert get_primes(0) == []
    assert get_primes(3) == [2, 3]
    assert get_primes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                              43, 47]
    assert get_primes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
