""" Give an algorithm for deleting an arbitrary element from min heap. """


class Heap:  # min heap
    def __init__(self):
        self.heapArr = [0]
        self.size = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heapArr[i] < self.heapArr[i // 2]:
                self.heapArr[i], self.heapArr[i // 2] = self.heapArr[i // 2], self.heapArr[i]
            i //= 2

    def append(self, k):
        self.heapArr.append(k)
        self.size += 1
        self.percolate_up(self.size)

    def min_index(self, i):
        if i * 2 + 2 > self.size:
            return i * 2 + 1
        else:
            if self.heapArr[i * 2 + 1] < self.heapArr[i * 2 + 2]:
                return i * 2 + 1
            else:
                return i * 2 + 2

    def percolate_down(self, i):
        while i * 2 + 1 <= self.size:
            index = self.min_index(i)
            if self.heapArr[index] < self.heapArr[i]:
                self.heapArr[index], self.heapArr[i] = self.heapArr[i], self.heapArr[index]

            i = index

    def delete_arbitrary(self, data):
        # search for the element in the heap
        if data not in self.heapArr:
            print(f"{data} not in heap")
        else:
            i = self.heapArr.index(data)
            self.heapArr[i], self.heapArr[-1] = self.heapArr[-1], self.heapArr[i]
            self.size -= 1
            self.heapArr.pop()
            self.percolate_down(i)


if __name__ == "__main__":
    heap = Heap()
    nums = [23, 31, 19, 10]

    [heap.append(nm) for nm in nums]
    print(f"Before deleting: {heap.heapArr[1:]}")
    heap.delete_arbitrary(19)
    print(f"After deleting: {heap.heapArr[1:]}")
