def quick_sort(A, low, high):
    if low < high:
        pivot = partition(A, low , high)
        quick_sort(A, low, pivot - 1)
        quick_sort(A, pivot + 1, high)


def partition(A, low, high):
    pivot = low
    swap(A, pivot, high)

    for i in range(low, high):
        if A[i] >= A[high]:
            swap(A, i, low)
            low += 1

    swap(A, low, high)
    return low


def swap(A, x, y):
    A[x], A[y] = A[y], A[x]


arr = [13, 21, 11, 19, 17, 14]
quick_sort(arr, 0, len(arr) - 1)
print(f"Sorted array:{arr}")
