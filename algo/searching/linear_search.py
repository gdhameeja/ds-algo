#!/usr/bin/env python3

def linear_search(arr, key):
    for index in range(len(arr)):
        if arr[index] == key:
            return index
    return -1

if __name__ == "__main__":
    arr = [4, 55, 101, 232, 444, 666, 777, 888, 901, 999, 1000, 1001, 1002, 2000, 4000, 10003, 20003, 232414]
    #arr = [x*2 for x in range(100000000)]
    assert linear_search(arr, 101) == 2
    print(linear_search(arr, 101))

