def countSubStringMatch(target, key):
    """Returns count of how many times ~key~ occurs in ~target~"""
    count = 0
    start_finding_index = 0

    while target.find(key, start_finding_index) != -1:
        count += 1
        start_finding_index = target.find(key, start_finding_index) + 1

    return count


def countSubStringMatchRecursive(target, key):
    """Returns count of how many times ~key~ occurs ~target~"""

    if target.find(key) == -1:
        return 0

    return 1 + countSubStringMatchRecursive(target[target.find(key)+1:], key)


def subStringMatchExact(target, key):
    """Returns tuple of starting indexes of ~key~ in ~target~"""
    index_tuple = ()
    start_finding_index = 0

    while target.find(key, start_finding_index) != -1:
        index_tuple += (target.find(key, start_finding_index), )
        start_finding_index = target.find(key, start_finding_index) + 1

    return index_tuple


def constrainedMatchPair(firstMatch, secondMatch, length):
    """Returns tuple of possible match of ~firstMatch~ + ~length~ + 1 is equal
       to ~secondMatch~"""
    possible_match = ()
    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k:
                possible_match += (n, )

    return possible_match


def getAllCombination(key):
    """Returns list of tuples with all possible combination of ~key~"""
    list_of_comb = []

    for i in range(len(key)):
        if i == 0:
            list_of_comb.append(('', key[1:]))

        if i > 0 and i < len(key):
            list_of_comb.append((key[0:i], key[i+1:]))

        if i == len(key):
            list_of_comb.append((key[:len(key)-1], ''))

    return list_of_comb


def subStringMatchExactlyOneSub(target, key):
    """Returns tuple of starting indexes of ~key~ in ~target~ where ~key~ is having
       one element substituted in ~target~"""
    all_key_combinations = getAllCombination(key)
    matching_pairs = ()

    for pair in all_key_combinations:
        index_pair = ((subStringMatchExact(target, pair[0]),
                       subStringMatchExact(target, pair[1])))

        matching_pairs += constrainedMatchPair(index_pair[0],
                                               index_pair[1],
                                               len(pair[0]))

    exact_matches = subStringMatchExact(target, key)

    exactly_one_subs = ()

    for p in matching_pairs:
        if p not in exact_matches:
            exactly_one_subs += (p,)

    return exactly_one_subs
