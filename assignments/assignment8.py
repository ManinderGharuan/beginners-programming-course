import time
VALUE, WORK = 0, 1


def loadSubjects(filename):
    """
    Returns dictionary of subject name to tuple of (value, work)
    """
    subjects = {}

    with open(filename) as sub_file:
        for line in sub_file:
            line_list = line.split(",")
            values = (int(line_list[1]), int(line_list[2]))
            subjects[line_list[0]] = tuple(values)

    return subjects


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]

    return val1 > val2


def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]

    return work1 < work2


def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]

    return float(val1) / float(work1) > float(val2) / float(work2)


def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns dictionary of subjects name to tuple of (value, work)
    """
    selected_subjects = {}

    while True:
        best_subject = None

        for subject in subjects.keys():
            if best_subject is None:
                best_subject = subject
            else:
                if best_subject in selected_subjects:
                    best_subject = subject
                else:
                    if comparator(subjects.get(subject),
                                  subjects.get(best_subject)):
                        best_subject = subject

        if maxWork >= subjects.get(best_subject)[WORK]:
            maxWork -= subjects.get(best_subject)[WORK]
            selected_subjects[best_subject] = subjects.get(best_subject)
        else:
            return selected_subjects


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = bruteForceAdvisorHelper(tupleList, maxWork,
                                                          0, None, None, [], 0,
                                                          0)
    outputSubjects = {}

    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]

    return outputSubjects


def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset is None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]

        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                            maxWork, i+1, bestSubset, bestSubsetValue, subset,
                            subsetValue + s[VALUE], subsetWork + s[WORK])

            subset.pop()

        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)

        return bestSubset, bestSubsetValue


def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time
    required to complete an answer
    """
    start_time = time.time()

    bruteForceAdvisor(subjects, maxWork)

    stop_time = time.time()
    total_time = stop_time - start_time

    print("If maximum work is {}, bruteForceAdvisor takes {} time to complete"
          .format(maxWork, total_time))


def dpBruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    memo = {}
    bestSubset, bestSubsetValue = dpBruteForceAdvisorHelper(tupleList, maxWork,
                                                            0, None, None, [],
                                                            0, 0, memo)
    outputSubjects = {}

    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]

    return outputSubjects


def dpBruteForceAdvisorHelper(subjects, maxWork, i, bestSubset,
                              bestSubsetValue, subset, subsetValue,
                              subsetWork, memo):

    key = ','.join([str(bestSubset), str(bestSubsetValue),
                    str(subsetWork), str(subsetValue)])

    if key in memo:
        return memo.get(key)

    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset is None or subsetValue > bestSubsetValue:
            # Found a new best.
            result = subset[:], subsetValue
            memo[key] = result

            return result
        else:
            # Keep the current best.
            result = bestSubset, bestSubsetValue
            memo[key] = result

            return result
    else:
        s = subjects[i]

        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = dpBruteForceAdvisorHelper(subjects,
                                                                    maxWork,
                                                                    i+1,
                                                                    bestSubset,
                                                                    bestSubsetValue,
                                                                    subset,
                                                                    subsetValue + s[VALUE],
                                                                    subsetWork + s[WORK],
                                                                    memo)

            subset.pop()

        bestSubset, bestSubsetValue = dpBruteForceAdvisorHelper(subjects,
                                                                maxWork,
                                                                i+1,
                                                                bestSubset,
                                                                bestSubsetValue,
                                                                subset,
                                                                subsetValue,
                                                                subsetWork,
                                                                memo)

        result = bestSubset, bestSubsetValue
        memo[key] = result

        return result


def dpAdvisor(subjects, maxWork):
    """
    Returns dictionary mapping subject name to (value, work)
    that contains a set of ~subjects~ that provides the maximum
    value without exceeding ~maxWork~.
    """
    return dpBruteForceAdvisor(subjects, maxWork)


def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an answer
    """
    start_time = time.time()

    dpAdvisor(subjects, maxWork)

    stop_time = time.time()
    total_time = stop_time - start_time

    print("If maximum work is {}, dpAdvisor takes {} time to complete"
          .format(maxWork, total_time))


if __name__ == "__main__":
    filename = "subjects.txt"
    subjects = loadSubjects(filename)
    maxWork = 10

    print(bruteForceTime())
    print(dpTime())
