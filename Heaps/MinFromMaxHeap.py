""" Insert into a Max Heap """


class Heap:  # Max Heap
    def __init__(self):
        self.heapArr = [0]
        self.size = 0

    def build_heap(self, A):
        index, self.size = len(A) // 2, len(A)
        self.heapArr = self.heapArr + A[:]

        while index > 0:
            self.percolate_down(index)
            index -= 1

    def min_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapArr[i * 2] < self.heapArr[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolate_down(self, i):
        while i * 2 <= self.size:
            index = self.min_index(i)
            if self.heapArr[index] > self.heapArr[i]:
                self.heapArr[index], self.heapArr[i] = self.heapArr[i], self.heapArr[index]

            i = index

    def min_in_max(self):
        minimum = self.heapArr[1]

        for i in range((self.size + 1) // 2, self.size + 1):
            if self.heapArr[i] < minimum:
                minimum = self.heapArr[i]
        return minimum


if __name__ == "__main__":
    heap = Heap()
    nums = [23, 31, 19, 10]
    heap.build_heap(nums)

    print(heap.heapArr[1:])
    print(f"Minimum: {heap.min_in_max()}")
