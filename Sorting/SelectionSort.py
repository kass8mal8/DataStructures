def selection_sort(A):
    for i in range(len(A)):
        for k in range(i + 1, len(A)):
            if A[k] < A[i]:
                A[i], A[k] = A[k], A[i]


arr = [13, 21, 11, 11, 17]
selection_sort(arr)
print(f"Sorted array:{arr}")
