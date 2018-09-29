#!/usr/bin/env python3

def count_sort(arr):
    maximum = max(arr) + 1   # finding the length of count array K where all numbers in arr >=0 and <=K

    count = [0] * maximum
    for i in arr:
        count[i] += 1

    # find the number of numbers less than or equal to the current number
    for i in range(1, len(count)):
        count[i] += count[i-1]

    result = [0] * len(arr)

    for i in arr:
        result[count[i] - 1] = i

    return result

if __name__ == "__main__":
    arr = [6, 2, 4, 9, 101, 1]

    # unit test
    assert count_sort(arr) == [1, 2, 4, 6, 9, 101]
    
    print(count_sort(arr))
