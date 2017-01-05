def get_min_index(ls):
    if not ls:
        return None

    count = 1
    min = ls[0]
    min_index = 0

    while count < len(ls):
        if min > ls[count]:
            min = ls[count]
            min_index = count

        count += 1

    return min_index


def selection_sort(ls):
    if len(ls) <= 1:
        return ls

    min_index = get_min_index(ls)

    ls[0], ls[min_index] = ls[min_index], ls[0]

    return [ls[0]] + selection_sort(ls[1:])


def bubble_sort(ls, have_changed=True):
    if not have_changed:
        return ls

    if len(ls) <= 1:
        return ls

    have_changed = False
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            ls[i], ls[i + 1] = ls[i + 1], ls[i]
            have_changed = True

    return bubble_sort(ls, have_changed)
