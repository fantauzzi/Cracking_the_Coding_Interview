import pytest
from stacks_balanced_brackets import is_matched
import random


def test_basic_1():
    s1 = '{[()]}'
    assert is_matched(s1)


def test_basic_2():
    s2 = '{[(])}'
    assert not is_matched(s2)


def test_basic_3():
    s3 = '{{[[(())]]}}'
    assert is_matched(s3)


def test_long():
    s = '{[({[' * 100 + ']})]}' * 100
    assert is_matched(s)


def test_a_1000_times():
    s = '{[({[]})]}' * 100
    for _ in range(1000):
        assert is_matched(s)


def test_a_1000_times_again():
    s = '()' * 500
    for _ in range(1000):
        assert is_matched(s)


def test_with_random_valid():
    # random.seed(42)
    s = ''
    tokens = {0: '()', 1: '[]', 2: '{}'}
    for _ in range(500):
        rnd = random.randint(0, 2)
        s = tokens[rnd][0] + s + tokens[rnd][1]
    assert is_matched(s)


def test_illegal_character():
    s = '{{[[(())]]}<}'
    with pytest.raises(ValueError):
        res = is_matched(s)


def test_purchased():
    s = {']}][}}(}][))]': False,
         '[](){()}': True,
         '()': True,
         '({}([][]))[]()': True,
         '{)[](}]}]}))}(())(': False}

    for item in s:
        assert is_matched(item) is s[item]


def test_from_disk():
    with open('test_data.txt', 'r') as data:
        with open('test_answers.txt','r') as answers:
            n = data.readline().rstrip('\n')
            for i in range(int(n)):
                s = data.readline().rstrip('\n')
                answer = answers.readline().rstrip('\n')
                assert answer in ('YES', 'NO')
                is_it_yes = True if answer == 'YES' else False
                assert is_matched(s) is is_it_yes
