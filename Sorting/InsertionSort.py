def insertion_sort(A):
    for i in range(1, len(A)):
        temp, k = A[i], i

        while k > 0 and temp < A[k - 1]:
            A[k] = A[k - 1]
            k -= 1

        A[k] = temp


arr = [13, 21, 26, 11, 17, 77, 31, 935]
insertion_sort(arr)
print(f"Sorted array:{arr}")
