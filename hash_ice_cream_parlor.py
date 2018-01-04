#!/bin/python3

def solve(arr, money):
    flavors = {}
    for i, cost in enumerate(arr):
        try:
            flavors[cost].append(i)
        except KeyError:
            flavors[cost] = [i]


    flavor_1, flavor_2 = None, None
    for amount in flavors:
        if amount >= money:
            continue
        remaining = money - amount
        try:
            available = flavors[remaining]
        except KeyError:
            available = []
        if len(available) > 1 and remaining == amount:
            assert len(available) == 2
            assert remaining == amount
            flavor_1, flavor_2 = available[0] + 1, available[1] + 1
            break
        if len(available) > 0:
            flavor_1 = available[0] + 1
            flavor_2 = flavors[amount][0] + 1
            break
    if flavor_1 is not None and flavor_2 is not None and flavor_1 > flavor_2:
        flavor_1, flavor_2 = flavor_2, flavor_1

    return flavor_1, flavor_2


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        flavor_1, flavor_2 = solve(arr, money)
        print(flavor_1, flavor_2)
