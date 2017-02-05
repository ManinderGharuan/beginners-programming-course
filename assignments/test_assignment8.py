from assignment8 import greedyAdvisor, cmpValue, cmpWork, cmpRatio


def test_greedyAdvisor():
    sub1 = {'6.00': (16, 8), '1.00': (7, 7),
            '6.01': (5, 3), '15.01': (9, 6)}
    sub2 = {'5.02': (1, 20), '5.05': (1, 14),
            '5.07': (2, 12), '5.09': (6, 18)}
    sub3 = {'24.07': (3, 15), '24.08': (2, 8),
            '24.09': (7, 14), '24.10': (2, 14)}

    assert greedyAdvisor(sub1, 15, cmpValue) == {'6.00': (16, 8),
                                                 '15.01': (9, 6)}
    assert greedyAdvisor(sub2, 10, cmpValue) == {}
    assert greedyAdvisor(sub3, 22, cmpValue) == {'24.09': (7, 14)}

    assert greedyAdvisor(sub1, 15, cmpWork) == {'6.01': (5, 3),
                                                '15.01': (9, 6)}
    assert greedyAdvisor(sub3, 15, cmpWork) == {'24.08': (2, 8)}
    assert greedyAdvisor(sub2, 15, cmpWork) == {'5.07': (2, 12)}

    assert greedyAdvisor(sub1, 15, cmpRatio) == {'6.00': (16, 8),
                                                 '6.01': (5, 3)}
    assert greedyAdvisor(sub2, 22, cmpRatio) == {'5.09': (6, 18)}
    assert greedyAdvisor(sub3, 10, cmpRatio) == {}
