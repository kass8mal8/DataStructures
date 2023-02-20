#  Iterative format


def binarySearch(arr, k):
    low, high = 0, len(arr)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return f"{k} Found at Index {mid}"
        else:
            if k > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

    if low > high:
        return None


A = [13, 17, 18, 20, 21, 24, 32]
print(binarySearch(A, 18))
