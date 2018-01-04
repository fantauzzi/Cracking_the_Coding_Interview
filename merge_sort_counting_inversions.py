#!/bin/python3

checks = 0


def count_inversions_bf(arr):
    # Complete this function
    if len(arr) <= 1:
        return 0
    total = 0
    for i in range(len(arr) - 1):
        for item in arr[i + 1:]:
            if arr[i] > item:
                total += 1

    return total


# @profile
def count_inversions_between(left, right):
    if len(left) == 0 or len(right) == 0:
        return 0
    i_r = 0
    res = 0
    for item in left:
        res += i_r
        while i_r < len(right) and item > right[i_r]:
            res += 1
            i_r += 1
    return res


# @profile
def merge_sorted(left, right):
    i_l, i_r = 0, 0
    sorted = []
    while i_l < len(left) and i_r < len(right):
        if left[i_l] <= right[i_r]:
            sorted.append(left[i_l])
            i_l += 1
        else:
            sorted.append(right[i_r])
            i_r += 1
    if i_l < len(left):
        sorted.extend(left[i_l:])
    elif i_r < len(right):
        sorted.extend(right[i_r:])
    return sorted


def count_and_sort(arr):
    assert len(arr) > 0
    if len(arr) == 1:
        return 0, arr
    elif len(arr) == 2:
        return (0, arr) if arr[0] <= arr[1] else (1, [arr[1]] + [arr[0]])
    arr_l = arr[0: len(arr) // 2]
    arr_r = arr[len(arr) // 2:]
    assert -1 <= len(arr_l) - len(arr_r) <= 1
    l_count, l_sorted = count_and_sort(arr_l)
    r_count, r_sorted = count_and_sort(arr_r)
    sorted = merge_sorted(l_sorted, r_sorted)
    straddling_count = count_inversions_between(l_sorted, r_sorted)
    return l_count + r_count + straddling_count, sorted


def main2():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result, _ = count_and_sort(arr)
        print(result)


def mai3():
    a = list(range(int(1e6), -1, -1))
    # a = list(range(int(1e5)))
    res, sorted = count_and_sort(a)
    assert res == sum(a)


def inversions(arr):
    n = len(arr)
    if n == 1:
        return 0
    n1 = n // 2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    ans = inversions(arr1) + inversions(arr2)
    i1 = 0
    i2 = 0
    for i in range(n):
        if i1 < n1 and (i2 >= n2 or arr1[i1] <= arr2[i2]):
            arr[i] = arr1[i1]
            ans += i2
            i1 += 1
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    return ans


def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = inversions(arr)
        print(result)


if __name__ == "__main__":
    main()
