""" Give an algorithm to find all elements Jess than some value of kin a binary heap. """


class Heap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]

            i //= 2

    def append(self, data):
        self.heapList.append(data)
        self.size += 1
        self.percolate_up(self.size)

    def less_than_value(self, i, k):
        while i * 2 <= self.size:
            if self.heapList[i] < k:
                print(self.heapList[i])

                self.less_than_value(i * 2 + 1, k)
                self.less_than_value(i * 2 + 2, k)
            i += 1


if __name__ == "__main__":
    heap = Heap()
    nums = [3, 5, 2, 4, 6]
    [heap.append(num) for num in nums]

    print(heap.heapList)
    print(heap.less_than_value(1, 4))
