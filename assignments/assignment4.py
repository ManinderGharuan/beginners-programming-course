from math import floor


def nestEggFixed(salary, save, growthRate, years):
    """Returns list of size of retirement account at the end of each year"""
    account_list = []

    for i in range(years):
        if i == 0:
            account_list.append(salary * save * 0.01)
        else:
            account_list.append((account_list[-1]) *
                                (1 + 0.01 * growthRate) +
                                (salary * save * 0.01))

    return account_list


def nestEggVariable(salary, salaryToSave, growthRates):
    """Returns list of size of retirement account at the end of each year"""
    account_list = []

    for i in range(len(growthRates)):
        if i == 0:
            account_list.append(salary * salaryToSave * 0.01)
        else:
            account_list.append((account_list[-1]) *
                                (1 + 0.01 * growthRates[i]) +
                                (salary * salaryToSave * 0.01))

    return account_list


def postRetirement(savings, growthRates, expenses):
    """Returns list of fund size after each year of retirement"""
    fund = []

    for i in range(len(growthRates)):
        if i == 0:
            fund.append(savings * (1 + 0.01 * growthRates[i]) - expenses)

        else:
            fund.append(fund[-1] * (1 + 0.01 * growthRates[i]) - expenses)

    return fund


def findMaxExpenses(salary, save, preRetireGrowthRates,
                    postRetireGrowthRates, epsilon):
    """Returns maximum estimate of expenses"""
    savings = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
    top = savings
    bottom = 0
    guess = (top + bottom) / 2
    remainingBal = postRetirement(savings, postRetireGrowthRates, guess)[-1]

    while abs(remainingBal) > epsilon:
        if remainingBal < 0:
            top = guess
        else:
            bottom = guess

        guess = (bottom + top) / 2
        remainingBal = postRetirement(savings,
                                      postRetireGrowthRates, guess)[-1]

    return floor(guess * 10 ** 8) / 10 ** 8
