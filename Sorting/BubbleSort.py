def bubble_sort(A):
    for i in range(len(A)):
        for k in range(len(A) - 1, i, -1):
            if A[k] < A[k - 1]:
                A[k], A[k - 1] = A[k - 1], A[k]


arr = [13, 21, 11, 19, 17]
bubble_sort(arr)
print(f"Sorted array:{arr}")
