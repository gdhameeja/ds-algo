#!/usr/bin/env python3

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":    
    arr = [4, 55, 101, 232, 444, 666, 777, 888, 901, 999, 1000, 1001, 1002, 2000, 4000, 10003, 20003, 232414]
    #arr = [x*2 for x in range(100000000)]
    assert binary_search(arr, 101) == 2
    print(binary_search(arr, 101))

    
