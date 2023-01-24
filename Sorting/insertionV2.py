def insertion_sort(A):
    for i in range(1, len(A)):
        tmp, k = A[i], i

        while k > 0 and tmp < A[k - 1]:
            A[k] = A[k - 1]
            k -= 1

        A[k] = tmp


arr = [13, 21, 11, 19, 15]
insertion_sort(arr)
print(arr)
