#  Recursive approach


def binarySearch(arr, k, low, high):
    if low > high:
        return
    else:
        mid = (low + high) // 2
        if arr[mid] == k:
            return f"{k} Found at Index {mid}"
        if k > arr[mid]:
            return binarySearch(arr, k, mid + 1, high)
        elif k < arr[mid]:
            return binarySearch(arr, k, low, mid - 1)
        else:
            return mid


A = [13, 17, 28, 29, 31, 36]
print(binarySearch(A, 29, 0, len(A)))
