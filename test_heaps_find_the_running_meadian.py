import random
from heaps_find_the_running_meadian import Rolling_median_finder


def test_rolling():
    finder = Rolling_median_finder()
    assert finder.roll(10) == 10
    assert finder.roll(20) == 15
    assert finder.roll(3) == 10
    assert finder.roll(30) == 15


def test_long():
    finder = Rolling_median_finder()
    for i in range(100000):
        finder.roll(random.randint(0,100000))
