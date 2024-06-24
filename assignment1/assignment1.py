# Name: Alex Clark
# OSU Email: clarka8@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 1 - Python Fundamentals Review
# Due Date: 01/29/24
# Description: Python Basics


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """Finds the minimum and maximum integers in a static array, and returns them as a tuple"""
    minimum = arr[0]
    maximum = arr[0]
    for i in range(arr.length()):
        if arr[i] < minimum:
            minimum = arr[i]
        if arr[i] > maximum:
            maximum = arr[i]
    return minimum, maximum

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Make a new array corresponding to values in the original. If num is divisible by 3, write fizz. If divisible by 5,
    write buzz. If both, write fizzbuzz, and if none just write num.
    """
    fizzbuzz_arr = StaticArray(arr.length())
    for i in range(arr.length()):
        if arr[i] % 3 == 0:
            fizzbuzz_arr[i] = "fizz"
            if arr[i] % 5 == 0:
                # Check if fizzbuzz
                fizzbuzz_arr[i] += "buzz"
        elif arr[i] % 5 == 0:
            fizzbuzz_arr[i] = "buzz"
        else:
            fizzbuzz_arr[i] = arr[i]
    return fizzbuzz_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Reverse numbers of an array in place
    """
    storage = 0
    for i in range(arr.length()//2):
        # Only need to go through half of the array; if array size is odd, middle is left alone
        storage = arr[i]
        arr[i] = arr[arr.length()-i-1]
        # Finds complimentary number in array
        arr[arr.length()-i-1] = storage


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """Creates a new array that has the values of the original array shifted by the step parameter"""
    stor = 0
    length = arr.length()
    rotated_arr = StaticArray(length)
    for i in range(arr.length()):
        # steps % length calculates the distance traveled. e.g if your steps are 24, and your array is size 6,
        # your elements won't actually move, so you use 24%6 and get 0.
        if i + steps % length > length - 1:
            # Make sure it loops at the end of the array
            pos = i + steps % length - length
        else:
            pos = i + steps % length
        rotated_arr[pos] = arr[i]
    return rotated_arr

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """Creates an array of all numbers in a given range"""
    length = abs(end - start)+1
    if start == end:
        length = 1
    arr = StaticArray(length)

    if start <= end:
        for i, value in enumerate(range(start, end+1)):
            arr[i] = value
    else:
        for i, value in enumerate(range(start, end-1, -1)):
            # Need to decrement if smaller number is first
            arr[i] = value
    return arr




# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Checks if an array is sorted. 1 = ascending or one element, -1 = descending, 0 = other
    """
    asc = True
    desc = True
    prev = arr[0]
    if arr.length() == 1:
        # If just one element
        return 1
    for i in range(1, arr.length()):
        # Ascending and Descending are exclusive, and you can't have both
        if prev < arr[i]:
            desc = False
        elif prev > arr[i]:
            asc = False
        elif prev == arr[i]:
            # No repeats
            asc = False
            desc = False
        prev = arr[i]
    if asc is True and desc is False:
        return 1
    elif asc is False and desc is True:
        return -1
    else:
        return 0


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Finds what element is the mode of the array, and how many times it occurs
    """
    top_element = arr[0]
    top_count = 1
    current_element = arr[0]
    current_count = 1
    for i in range(1, arr.length()):
        if current_element == arr[i]:
            # Increment if multiple of the same number
            current_count += 1
        else:
            # If there is a new number, check if the current count is higher, and if so, make it the new mode
            if current_count > top_count:
                top_count = current_count
                top_element = current_element
            current_count = 1
            current_element = arr[i]
    if current_count > top_count:
        # Case for last element of the array; there is no next number to check so the current count needs to be checked
        top_count = current_count
        top_element = current_element
    return top_element, top_count



# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Creates a new array that removes all duplicates from the input array
    """
    counter = 1
    for i in range(1, arr.length()):
        if arr[i-1] != arr[i]:
            counter += 1
            # Find array size for output array
    no_dupes_arr = StaticArray(counter)
    j = 0
    for i in range(1, arr.length()):
        if arr[i-1] != arr[i]:
            no_dupes_arr[j] = arr[i-1]
            j += 1
    no_dupes_arr[counter-1] = arr[arr.length()-1]
    return no_dupes_arr




# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """Sorts integers in descending order, using an array to count occurrences"""
    min, max = min_max(arr)
    k = max - min + 1
    # Array size for counting array
    count_arr = StaticArray(k)
    for i in range(k):
        count_arr[i] = 0

    for i in range(arr.length()):
        count_arr[arr[i]-min] += 1
        # Add in counts per value, adjusted by minimum value to allow for negatives
    output_arr = StaticArray(arr.length())
    j = 0
    for i in range(k):
        # For each i in count, add i to the output array count[i] times, incrementing the output array index each time.
        for _ in range(count_arr[i]):
            output_arr[j] = i+min
            # Add back min, so index 0 is actually the index of the minimum number
            j += 1
    reverse(output_arr)
    # Reverse to descending order
    return output_arr

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Take a sorted list of numbers, and output a descending array of the squares of the numbers
    """
    length = arr.length()
    sorted_arr = StaticArray(length)
    left, right = 0, length-1
    i = length - 1
    # Sorted array is filled from right to left
    while left <= right:
        # If the left and right index "pass" each other, the whole array has been processed
        left_sq = arr[left] ** 2
        right_sq = arr[right] ** 2
        # Indexes go towards the center, and left and right are compared. This is so negative numbers with high squares
        # are sorted correctly
        #   l ->          <- r
        # [-3, -2, -2, 0, 1, 2]
        # -3^2=9 > 2^2=4, so the left index advances to the second value
        if left_sq > right_sq:
            sorted_arr[i] = left_sq
            left += 1
            # If left was larger, more to the left (possible negative numbers that may be larger than the right)
            # need to be checked before the right
        else:
            sorted_arr[i] = right_sq
            right -= 1
        i -= 1
    return sorted_arr
# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
