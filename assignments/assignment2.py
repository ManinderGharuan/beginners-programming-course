def is_possible(num, i=6, j=9, k=20):
    """Returns True if it is possible to make combination of ~i~, ~j~ and ~k~ which
       is equal to ~num~"""

    for a in range(num):
        for b in range(num):
            for c in range(num):
                if (i*a + j*b + k*c) == num:
                    return True

    return False


def max_impossible(i=6, j=9, k=20):
    """Returns maximum number which cannot be made with combination of ~i~, ~j~ &
       ~k~"""
    count = 0
    not_possible = 1
    max_impossible = not_possible

    while True:
        if is_possible(not_possible, i, j, k):
            count += 1
        else:
            max_impossible = not_possible
            count = 0

        if count == 6:
            return max_impossible

        not_possible += 1
