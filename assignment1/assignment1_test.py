import pytest
from static_array import *
from assignment1 import *


def test_min_max():
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    res = min_max(arr)
    print(res)
    assert res[0] == -5 and res[1] == 8


def test_fizz_buzz():
    source = [_ for _ in range(-5, 20, 4)]
    res = ['buzz', -1, 'fizz', 7, 11, 'fizzbuzz', 19]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    res_arr = StaticArray(len(res))
    for i, value in enumerate(res):
        res_arr[i] = value
    assert print(fizz_buzz(arr)) == print(res_arr)

def test_reverse():
    source = [-20, -13, -6, 1, 3, 8, 15]
    res = [15, 8, 3, 1, -6, -13, -20]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    res_arr = StaticArray(len(res))
    for i, value in enumerate(res):
        res_arr[i] = value
    reverse(arr)
    assert print(arr) == print(res_arr)

def test_rotate():
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = ' ' if steps >= 0 else ''
        print(f'{rotate(arr, steps)}{space}{steps}')
    print(arr)