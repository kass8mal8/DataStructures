arr = [11, 13, 21, 19]

for x in range(len(arr)):
    for i in range(x, len(arr)):
    if arr[x] > arr[0]:
        arr[x], arr[0] = arr[0], arr[x]
        x += 1

print(arr)
