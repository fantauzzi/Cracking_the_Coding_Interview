from collections import Counter


def ransom_note(magazine, ransom):
    magazine_count = Counter(magazine)
    ransom_count = Counter(ransom)
    not_found = ransom_count - magazine_count
    return False if sum(not_found.values()) > 0 else True


def test_basic_yes():
    magazine = 'give me one grand today night'.split()
    ransom = 'give one grand today'.split()
    res = ransom_note(magazine, ransom)
    assert res


def test_basic_no():
    magazine = 'two times three is not four'.split()
    ransom = 'two times two is four'.split()
    res = ransom_note(magazine, ransom)
    assert not res


if __name__ == '__main__':
    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if (answer):
        print("Yes")
    else:
        print("No")

