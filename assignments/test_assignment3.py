from assignment3 import (countSubStringMatch,
                         countSubStringMatchRecursive,
                         subStringMatchExact,
                         constrainedMatchPair,
                         getAllCombination,
                         subStringMatchExactlyOneSub)


t1 = 'atgacatgcacaagtatgcat'
t2 = 'abcsjabcjfkabcjflskfabcjfsabc'
t3 = 'mkdsfxyzfjksdfzxysjkxyzjkd'
t4 = 'jfsabcdabcdjkdfabcd'

k1 = 'dfg'
k2 = 'atgc'
k3 = 'abc'
k4 = 'xyz'
k5 = 'abcd'


def test_countSubStringMatch():
    assert countSubStringMatch(t1, k1) == 0
    assert countSubStringMatch(t1, k2) == 2
    assert countSubStringMatch(t2, k3) == 5
    assert countSubStringMatch(t3, k4) == 2
    assert countSubStringMatch(t4, k5) == 3


def test_countSubStringMatchRecursive():
    assert countSubStringMatchRecursive(t1, k1) == 0
    assert countSubStringMatchRecursive(t1, k2) == 2
    assert countSubStringMatchRecursive(t2, k3) == 5
    assert countSubStringMatchRecursive(t3, k4) == 2
    assert countSubStringMatchRecursive(t4, k5) == 3


def test_subStringMatchExact():
    assert subStringMatchExact(t1, k1) == ()
    assert subStringMatchExact(t1, k2) == (5, 15)
    assert subStringMatchExact(t2, k3) == (0, 5, 11, 20, 26)
    assert subStringMatchExact(t3, k4) == (5, 20)
    assert subStringMatchExact(t4, k5) == (3, 7, 15)


def test_getAllCombination():
    assert getAllCombination('at') == [('', 't'),
                                       ('a', '')]
    assert getAllCombination('abc') == [('', 'bc'),
                                        ('a', 'c'),
                                        ('ab', '')]
    assert getAllCombination('abcd') == [('', 'bcd'),
                                         ('a', 'cd'),
                                         ('ab', 'd'),
                                         ('abc', '')]
    assert getAllCombination('abcde') == [('', 'bcde'),
                                          ('a', 'cde'),
                                          ('ab', 'de'),
                                          ('abc', 'e'),
                                          ('abcd', '')]


def test_constrainedMatchPair():
    t = 'sabsdefjkabcdkdjibcdefskjdfabcdjf'

    m1a, m1b = '', 'bcdef'
    m1as = subStringMatchExact(t, m1a)
    m1bs = subStringMatchExact(t, m1b)

    m2a, m2b = 'a', 'cdef'
    m2as = subStringMatchExact(t, m2a)
    m2bs = subStringMatchExact(t, m2b)

    m3a, m3b = 'ab', 'def'
    m3as = subStringMatchExact(t, m3a)
    m3bs = subStringMatchExact(t, m3b)

    assert constrainedMatchPair(m1as, m1bs, len(m1a)) == (16, )
    assert constrainedMatchPair(m2as, m2bs, len(m2a)) == ()
    assert constrainedMatchPair(m3as, m3bs, len(m3a)) == (1, )


def test_subStringMatchExactlyOneSub():
    t3 = 'atgacatgcacaagtatgcat'
    k1 = 'atga'

    t1 = 'sabsdefjkabcdkdjibcdefskjdfabcdjf'
    k2 = 'abcdef'

    t2 = 'abuabcxyhxyzbcxjzaxczxyz'
    k3 = 'abc'
    k4 = 'xyz'

    assert subStringMatchExactlyOneSub(t3, k1) == (5, 15)
    assert subStringMatchExactlyOneSub(t1, k2) == (16, 1, 27)
    assert subStringMatchExactlyOneSub(t2, k3) == (11, 17, 0)
    assert subStringMatchExactlyOneSub(t2, k4) == (14, 18, 6)
