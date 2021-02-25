#!/usr/bin/env python3

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    arr1 = [5, 3, 11, 101, 1, 7]
    arr2 = [1, 2, 3, 4, 5]

    # unit test
    assert insertion_sort(arr1) == [1, 3, 5, 7, 11, 101]
    assert insertion_sort(arr2) == [1, 2, 3, 4, 5]

    print(insertion_sort(arr1))
    print(insertion_sort(arr2))
