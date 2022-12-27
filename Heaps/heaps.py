"""Maximum Heap"""


class Heap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.heapList[index] < self.heapList[index // 2]:
                self.heapList[index], self.heapList[index // 2] = self.heapList[index // 2], self.heapList[index]

            index //= 2

    def min_index(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heapList[index * 2] < self.heapList[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def percolate_down(self, index):
        while index * 2 <= self.size:
            min_child = self.min_index(index)
            if self.heapList[index] < self.heapList[min_child]:
                self.heapList[index], self.heapList[min_child] = self.heapList[min_child], self.heapList[index]

            index = min_child

    def append(self, data):
        self.heapList.append(data)
        self.size += 1
        self.percolate_up(self.size)

    def delete_max(self):
        # temp = self.heapList[1]
        self.heapList[1], self.heapList[self.size] = self.heapList[self.size], self.heapList[1]
        self.size -= 1
        self.heapList.pop()
        self.percolate_down(1)


if __name__ == "__main__":
    heap = Heap()
    nums = [12, 32, 43, 95, 30]
    [heap.append(num) for num in nums]
    print(heap.heapList)
    heap.delete_max()
    print(heap.heapList)
