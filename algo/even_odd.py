def even_odd(arr):
    left, right = 0, len(arr) - 1
    while left != right:
        if arr[left] % 2 == 0:
            # even case
            left += 1
        else:
            # odd case
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1

def test(arr):
    is_odd = False
    for each in arr:
        if each % 2 == 0:
            # even case
            if is_odd:
                return False
        else:
            # odd case
            if not is_odd:
                is_odd = True
    return True


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_odd(arr)
    assert test(arr) == True, "All tests failed!"
    print("All tests passed")
