def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left, right = A[:mid], A[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


arr = [13, 21, 11, 19, 17, 14]
merge_sort(arr)
print(f"Sorted array:{arr}")
