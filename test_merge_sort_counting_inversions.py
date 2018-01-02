from merge_sort_counting_inversions import count_inversions_between, merge_sorted, count_inversions_bf, count_and_sort


def test_two_fingers():
    a = [1, 3, 5, 6]
    b = [2, 4, 6, 8]
    assert merge_sorted(a, b) == [1, 2, 3, 4, 5, 6, 6, 8]


def test_count_inversions_small():
    a = [0, 2]
    b = [1, 3]
    assert count_inversions_between(a, b) == 1


def test_count_inversions():
    a = [1, 3, 4, 6]
    b = [1, 2, 3, 3]
    assert count_inversions_between(a, b) == 10


def test_small_count_and_sort():
    a = [0, 2, 1, 3]
    count, _ = count_and_sort(a)
    assert 1 == count


def test_quick_and_bf():
    a = [1, 3, 7, 2, 4, 6]
    count, _ = count_and_sort(a)
    count_bf = count_inversions_bf(a)
    assert count_bf == count


def test_none():
    a = list(range(10))
    assert count_inversions_bf(a) == 0


def test_single():
    a = [0, 1, 3, 5, 4, 6, 7, 8]
    assert count_inversions_bf(a) == 1


def test_multiple():
    a = [2, 1, 3, 1, 2]
    assert count_inversions_bf(a) == 4
    res, _ = count_and_sort(a)
    assert res == 4


def test_all():
    a = list(range(9, -1, -1))
    assert count_inversions_bf(a) == sum(a)
    res, _ = count_and_sort(a)
    assert res == sum(a)


def test_load():
    a = list(range(int(1e6)))
    res, sorted = count_and_sort(a)
    assert res == 0


def test_load_reverse():
    a = list(range(int(1e6), -1, -1))
    res, sorted = count_and_sort(a)
    assert res == sum(a)

