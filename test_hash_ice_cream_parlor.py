from hash_ice_cream_parlor import solve

def test_hackerrank_1():
    flavor_1, flavor_2 = solve([1, 4, 5, 3, 2], 4)
    assert (1, 4) == (flavor_1, flavor_2)


def test_hackerrank_2():
    flavor_1, flavor_2 = solve([2, 2, 4, 3], 4)
    assert (1, 2) == (flavor_1, flavor_2)
