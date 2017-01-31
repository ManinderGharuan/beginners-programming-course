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


def merge(left, right):
    """joins sorted list left and right return new sorted list"""
    merge_list = []
    i, j = 0, 0

    while True:
        if j == len(right):
            merge_list.extend(left[i:])
            break

        if i == len(left):
            merge_list.extend(right[j:])
            break

        if left[i] > right[j]:
            merge_list.append(right[j])
            j += 1
        else:
            merge_list.append(left[i])
            i += 1

    return merge_list


def merge_sort(ls):
    if len(ls) < 2:
        return ls

    mid = len(ls) // 2
    left = merge_sort(ls[:mid])
    right = merge_sort(ls[mid:])

    return merge(left, right)
