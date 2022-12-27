""" Insert into a Max Heap """


class Heap:  # Min Heap
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i //= 2

    def append(self, k):
        self.heapList.append(k)
        self.size += 1
        self.percolate_up(self.size)

    def min_in_max(self):
        minimum = self.heapList[1]

        for i in range((self.size + 1) // 2, self.size + 1):
            if self.heapList[i] < minimum:
                minimum = self.heapList[i]
        return minimum


if __name__ == "__main__":
    heap = Heap()
    nums = [23, 31, 19, 10]

    [heap.append(nm) for nm in nums]
    print(heap.heapList)
    print(f"Minimum: {heap.min_in_max()}")
