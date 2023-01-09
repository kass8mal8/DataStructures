""" Give an algorithm for merging two binary max-heaps. Let us assume that the size of the first
heap is m+ n and the size of the second heap is n. """


class Heap:  # Max Heap
    def __init__(self):
        self.heapArr = [0]
        self.size = 0

    def max_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapArr[i * 2] > self.heapArr[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heapArr[i] > self.heapArr[i // 2]:
                self.heapArr[i], self.heapArr[i // 2] = self.heapArr[i // 2], self.heapArr[i]

            i //= 2

    def percolate_down(self, i):
        while i * 2 + 1 <= self.size:
            index = self.max_index(i)

            if self.heapArr[i] < self.heapArr[index]:
                self.heapArr[i], self.heapArr[index] = self.heapArr[index], self.heapArr[i]

            i = index

    def append(self, k):
        self.heapArr.append(k)
        self.size += 1
        self.percolate_up(self.size)


class Solution(Heap):
    def __init__(self):
        super().__init__()
        self.arr = [0]
        self.size = 0

    def merge_heaps(self, H1, H2):
        arr = H1 + H2[:]

        # find first non leaf node
        i = (len(arr) - 2) // 2
        self.percolate_down(i)

        return arr


if __name__ == "__main__":
    heap = Heap()
    heap1 = Heap()
    sltn = Solution()

    nums = [12, 32, 43]
    nms = [95, 30, 11]

    [heap.append(num) for num in nums]
    [heap1.append(nm) for nm in nms]

    print(heap.heapArr[1:])
    print(heap1.heapArr[1:])

    print(f"Merged Heap: {sltn.merge_heaps(heap, heap1)}")

