from assignment1 import is_prime, get_primes, prime_log_sum


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


def test_prime_log_sum():
    assert prime_log_sum(0) == (0, 0, 0)
    assert prime_log_sum(3) == (0.7781512503836436, 3, 0.25938375012788123)
    assert prime_log_sum(50) == (17.78879727658294, 50, 0.3557759455316588)
    assert prime_log_sum(30) == (9.810883688446632, 30, 0.3270294562815544)
