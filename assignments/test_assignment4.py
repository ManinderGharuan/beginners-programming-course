from assignment4 import (nestEggFixed,
                         nestEggVariable,
                         postRetirement,
                         findMaxExpenses)


def test_nestEggFixed():
    salary1 = 10000
    salary2 = 15000

    save1 = 5
    save2 = 10
    save3 = 15

    grate1 = 15
    grate2 = 10
    grate3 = 18

    year1 = 5
    year2 = 3
    year3 = 8

    assert nestEggFixed(salary1, save2, grate1, year1) == [1000.0,
                                                           2150.0,
                                                           3472.5,
                                                           4993.375,
                                                           6742.3812499999995]
    assert nestEggFixed(salary1, save1, grate1, year1) == [500.0,
                                                           1075.0,
                                                           1736.25,
                                                           2496.6875,
                                                           3371.1906249999997]
    assert nestEggFixed(salary2, save1, grate2, year3) == [750.0,
                                                           1575.0,
                                                           2482.5,
                                                           3480.75,
                                                           4578.825000000001,
                                                           5786.707500000001,
                                                           7115.378250000002,
                                                           8576.916075000001]
    assert nestEggFixed(salary1, save3, grate2, year2) == [1500.0,
                                                           3150.0,
                                                           4965.0]
    assert nestEggFixed(salary2, save1, grate3, year1) == [750.0,
                                                           1635.0,
                                                           2679.3,
                                                           3911.574,
                                                           5365.65732]
    assert nestEggFixed(salary1, save2, grate1, year3) == [1000.0,
                                                           2150.0,
                                                           3472.5,
                                                           4993.375,
                                                           6742.381249999999,
                                                           8753.738437499998,
                                                           11066.799203124998,
                                                           13726.819083593746]


def test_nestEggVariable():
    salary1 = 10000
    salary2 = 15000

    save1 = 5
    save2 = 10
    save3 = 15

    grate1 = 15
    grate2 = 10
    grate3 = 18
    grate4 = 12
    grate5 = 20
    grate6 = 8

    growthRates = [3, 4, 5, 0, 3]

    lsgrow1 = [grate1, grate2, grate3, grate4]
    lsgrow2 = [grate6, grate1, grate3, grate5, grate1]
    lsgrow3 = [grate5, grate5, grate3, grate1, grate2, grate4]

    assert nestEggVariable(salary1, save2, growthRates) == [1000.0,
                                                            2040.0,
                                                            3142.0,
                                                            4142.0,
                                                            5266.2600000000002]
    assert nestEggVariable(salary1, save2, lsgrow1) == [1000.0,
                                                        2100.0,
                                                        3478.0,
                                                        4895.360000000001]
    assert nestEggVariable(salary2, save3, lsgrow2) == [2250.0,
                                                        4837.5,
                                                        7958.25,
                                                        11799.9,
                                                        15819.884999999998]
    assert nestEggVariable(salary2, save1, lsgrow3) == [750.0,
                                                        1650.0,
                                                        2697.0,
                                                        3851.5499999999997,
                                                        4986.705,
                                                        6335.109600000001]
    assert nestEggVariable(salary1, save3, lsgrow2) == [1500.0,
                                                        3225.0,
                                                        5305.5,
                                                        7866.599999999999,
                                                        10546.589999999998]
    assert nestEggVariable(salary2, save1, lsgrow1) == [750.0,
                                                        1575.0,
                                                        2608.5,
                                                        3671.5200000000004]


def test_postRetirement():
    sav1 = 200000
    sav2 = 500000
    sav3 = 100000
    sav4 = 250000

    lsgrate1 = [3, 5, 7, 2, 1]
    lsgrate2 = [7, 2, 7, 2]
    lsgrate3 = [1, 6, 3, 6, 2, 6]
    lsgrate4 = [10, 5, 0, 5, 1]

    ex1 = 50000
    ex2 = 20000
    ex3 = 10000
    ex4 = 30000

    assert postRetirement(sav3, lsgrate4, ex4) == [80000.000000000015,
                                                   54000.000000000015,
                                                   24000.000000000015,
                                                   -4799.9999999999854,
                                                   -34847.999999999985]
    assert postRetirement(sav1, lsgrate3, ex3) == [192000.0,
                                                   193520.0,
                                                   189325.6,
                                                   190685.13600000003,
                                                   184498.83872000003,
                                                   185568.76904320004]
    assert postRetirement(sav2, lsgrate3, ex3) == [495000.0,
                                                   514700.0,
                                                   520141.0,
                                                   541349.4600000001,
                                                   542176.4492000001,
                                                   564707.0361520002]
    assert postRetirement(sav4, lsgrate3, ex1) == [202500.0,
                                                   164650.0,
                                                   119589.5,
                                                   76764.87000000001,
                                                   28300.167400000006, -
                                                   20001.822555999992]
    assert postRetirement(sav3, lsgrate2, ex2) == [87000.0,
                                                   68740.0,
                                                   53551.8,
                                                   34622.836]
    assert postRetirement(sav4, lsgrate1, ex3) == [247500.0,
                                                   249875.0,
                                                   257366.25,
                                                   252513.575,
                                                   245038.71075000003]
    assert postRetirement(sav2, lsgrate1, ex3) == [505000.0,
                                                   520250.0,
                                                   546667.5,
                                                   547600.85,
                                                   543076.8585]


def test_findMaxExpenses():
    salary = 10000
    save = 10
    preRetireGrowthRates = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon = .01

    assert findMaxExpenses(salary, save, preRetireGrowthRates,
                           postRetireGrowthRates, epsilon) == 1229.95548986
