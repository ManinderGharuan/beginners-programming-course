from algorithms import get_min_index, selection_sort, bubble_sort


def test_get_min_index():
    assert get_min_index([]) is None
    assert get_min_index([2]) == 0
    assert get_min_index([3, 5, 2, 7]) == 2
    assert get_min_index([6, 4, 7, 5, 6, 2]) == 5
    assert get_min_index([6, 9, 7, 5, 6]) == 3


def test_selection_sort():
    assert selection_sort([]) == []
    assert selection_sort([2]) == [2]
    assert selection_sort([3, 5, 6, 7, 4, 2]) == [2, 3, 4, 5, 6, 7]
    assert selection_sort([7, 4, 5, 3, 2, 6]) == [2, 3, 4, 5, 6, 7]


def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([2]) == [2]
    assert bubble_sort([3, 5, 6, 7, 4, 2]) == sorted([3, 5, 6, 7, 4, 2])
    assert bubble_sort([7, 4, 5, 3, 2, 6]) == sorted([7, 4, 5, 3, 2, 6])
