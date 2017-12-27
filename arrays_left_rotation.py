import pytest

def array_left_rotation(the_array, count):
    """
    Rotates a list to the left of n positions.
    :param the_array: the list to be rotated.
    :param count: the number of rotations
    :return: the rotated list
    """

    if count < 0:
        raise ValueError('Negative parameter not allowed, got value {}'.format(count))

    if len(the_array) > 0:
        count = count % len(the_array)
    the_array = the_array[count:] + the_array[0:count]
    return the_array

def test_basic():
    a=[1, 2, 3, 4, 5]
    r1 = array_left_rotation(a, 4)
    assert r1 == [5, 1, 2, 3, 4]

def test_null():
    a = [1, 2, 3, 4, 5]
    r1 = array_left_rotation(a, 0)
    assert r1 == a

def test_2_cycles():
    a = [1, 2, 3, 4, 5]
    r1 = array_left_rotation(a, 10)
    assert r1 == a

def test_empty():
    a = []
    r1 = array_left_rotation(a, 10)
    assert r1 == []

def test_long():
    a1 = list(range(10000))
    a2 = list(range(10000))
    r1 = array_left_rotation(a1, len(a1)+1)
    r2 = array_left_rotation(a2, len(a2)*2+1)
    assert r1 == r2

def test_negative_count():
    with pytest.raises(ValueError):
        array_left_rotation([1,2], -1)

def test_original_unchanged():
    a = [1, 2, 3, 4, 5]
    r = array_left_rotation(a, 1)
    assert r != a
    assert r is not a

if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = array_left_rotation(a, k);
    print(*answer, sep=' ')
