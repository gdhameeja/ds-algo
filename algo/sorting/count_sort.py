#!/usr/bin/python3


def count_sort(arr):
    max_num = max(arr)
    count = [0] * 10

    for i in arr:
        count[i-1] += 1

    # prefix sum to get the number of elements less than the current element.
    for i in range(1, 10):
        count[i] += count[i-1]

    result = [0] * len(arr)

    for i in reversed(range(0, len(arr))):
        result[count[arr[i]-1]-1] = arr[i]
        count[arr[i]-1] -= 1

    return result

if __name__ == "__main__":
    array = [5, 6, 1, 2, 7, 9]
    print(count_sort(array))
