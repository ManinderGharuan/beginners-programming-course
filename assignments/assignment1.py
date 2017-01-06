def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def get_primes(num):
    primes = []

    for i in range(num + 1):
        if is_prime(i):
            primes.append(i)

    return primes
