""" Dynamic median finding. Design a heap data structure that supports finding the median. """


class MinHeap:
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

    def percolate_down(self, i):
        while i * 2 <= self.size:
            index = self.min_index(i)
            if self.heapArr[index] < self.heapArr[i]:
                self.heapArr[index], self.heapArr[i] = self.heapArr[i], self.heapArr[index]

            i = index

    def build_heap(self, A):
        index, self.size = len(A) // 2, len(A)
        self.heapArr = self.heapArr + A[:]

        while index > 0:
            self.percolate_down(index)
            index -= 1


class MaxHeap:
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

    def percolate_down(self, i):
        while i * 2 <= self.size:
            index = self.max_index(i)
            if self.heapArr[index] > self.heapArr[i]:
                self.heapArr[index], self.heapArr[i] = self.heapArr[i], self.heapArr[index]

            i = index

    def build_heap(self, A):
        index, self.size = len(A) // 2, len(A)
        self.heapArr = self.heapArr + A[:]

        while index > 0:
            self.percolate_down(index)
            index -= 1


if __name__ == "__main__":
    minHeap = MinHeap()
    maxHeap = MaxHeap()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = (len(nums) + 1) // 2

    def median(mn, mx):
        mx.build_heap(nums[:k])
        mn.build_heap(nums[k:])

        if len(mn.heapArr) == len(mx.heapArr):
            avg = (mn.heapArr[1] + mx.heapArr[1]) / 2
            return avg
        else:
            return mx.heapArr[1]

    print(f"Median: {median(minHeap, maxHeap)}")
