def partition(A, low, high):
    pivot = A[low]
    start, end = low + 1, high

    while True:
        while A[low] < pivot and start < end:
            start += 1

        while A[end] > pivot and end >= low:
            end -= 1

        if start < end:
            A[start], A[end] = A[end], A[start]

        return low


def quick_sort(A, low, high):
    if low < high:
        pivot = partition(A, low, high)
        quick_sort(A, low, pivot - 1)
        quick_sort(A, pivot + 1, high)


arr = [13, 21, 19, 11]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
