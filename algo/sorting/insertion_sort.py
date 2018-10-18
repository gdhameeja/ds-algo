#!/usr/bin/env python3

def insertion_sort(arr):
    i = 1
    while i < len(arr):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        i += 1
    return arr

if __name__ == "__main__":
    arr = [5, 3, 11, 101, 1, 7]

    # unit test
    assert insertion_sort(arr) == [1, 3, 5, 7, 11, 101]

    print(insertion_sort(arr))
