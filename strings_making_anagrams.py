from collections import Counter

''' Here my first solution. It is not as efficient as it could be '''

def number_needed2(a, b):
    """
    Given two strings, consisting of lowercase English alphabetic letters, determine the minimum number of character deletions required to make them anagrams. Any characters can be deleted from either of the strings. The length of either string cannot exceed 10000 characters.
    :param a: one of the two given strings.
    :param b: the other given string.
    :return: the minimum number of character deletions required to make the two strings anagram.
    """
    a = sorted(a)
    b = sorted(b)
    i_a, i_b = 0, 0
    res = 0
    while i_a <= len(a)-1 and i_b <= len(b)-1:
        if a[i_a] == b[i_b]:
            i_a += 1
            i_b += 1
        else:
            res += 1
            if a[i_a] < b[i_b]:
                i_a += 1
            else:
                i_b += 1
    res += len(b)-i_b if i_a == len(a) else len(a)-i_a
    return res

''' This is a more efficient, and more compact, solution'''

def number_needed(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    res = sum((count_a - count_b).values()) + sum((count_b - count_a).values())
    return res


def test_basic():
    res = number_needed('cde', 'abc')
    assert res == 4


def test_longer():
    res = number_needed('dacbc', 'fecbbc')
    assert res == 5


def test_5_and_10():
    res = number_needed('deacb', 'dbeacxyzwv')
    assert res == 5


def test_real_long():
    a = 'deacb'*1000
    b = 'dbeacxyzwv'*1000
    res = number_needed(a, b)
    assert res == 5000


def test_empty():
    r1 = number_needed('', '')
    assert r1 == 0
    r2 = number_needed('', 'ajtujkxoop')
    assert r2 == 10
    r3 = number_needed('xxp', '')
    assert r3 == 3


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()

    print(number_needed(a, b))
