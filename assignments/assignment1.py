from math import log10 as log


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


def prime_log_sum(num):
    logs = []
    logs_sum = 0

    if num == 0:
        return (0, 0, 0)

    for i in get_primes(num):
        logs.append(log(i))

    for i in logs:
        logs_sum += i

    logs_sum_ratio_num = logs_sum / num

    return (logs_sum, num, logs_sum_ratio_num)
