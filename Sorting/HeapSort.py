class Heap:
    def __init__(self):
        self.heapArr = [0]
        self.size = 0

    def min_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapArr[i * 2] < self.heapArr[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolateDown(self, i):
        while i * 2 <= self.size:
            index = self.min_index(i)

            if self.heapArr[index] < self.heapArr[i]:
                self.swap(self.heapArr, index, i)

            i = index

    def buildHeap(self, A):
        index, self.size = len(A) // 2, len(A)
        self.heapArr = self.heapArr + A[:]

        while index > 0:
            self.percolateDown(index)
            index -= 1

    @staticmethod
    def swap(A, x, y):
        if x != y:
            A[x], A[y] = A[y], A[x]


if __name__ == "__main__":
    heap = Heap()
    arr = [13, 28, 11, 19, 9]

    heap.buildHeap(arr)
    print(heap.heapArr[1:])
