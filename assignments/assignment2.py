def is_possible(num, i=6, j=9, k=20):
    """Returns True if it is possible to make combination of 6, 9 and 20 which
       is equal to ~number~"""

    for a in range(num):
        for b in range(num):
            for c in range(num):
                if (i*a + j*b + k*c) == num:
                    return True

    return False


def max_impossible(num, i=6, j=9, k=20):
    """Returns Last ~number~ which cannot possible to make combination of 6, 9
       and 20"""
    count = 0
    not_possible = 0

    for n in range(num):
        if is_possible(n, i, j, k):
            count += 1
        else:
            count = 0
            not_possible = n

        if count == 6:
            return not_possible
