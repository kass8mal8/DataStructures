""" Give an algorithm for deleting the kth indexed element in a given min-heap. """


class Heap:  # min Heap
    def __init__(self):
        self.arr = [0]
        self.size = 0

    def min_index(self, i):
        if i * 2 + 2 > self.size:
            return i * 2 + 1
        else:
            if self.arr[i * 2 + 1] > self.arr[i * 2 + 2]:
                return i * 2 + 2
            else:
                return i * 2 + 1

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.arr[i] < self.arr[i // 2]:
                self.arr[i], self.arr[i // 2] = self.arr[i // 2], self.arr[i]

            i //= 2

    def percolate_down(self, i):
        while i * 2 < self.size:
            index = self.min_index(i)

            if self.arr[index] < self.arr[i]:
                self.arr[index], self.arr[i] = self.arr[i], self.arr[index]

    def append(self, data):
        self.arr.append(data)
        self.size += 1
        self.percolate_up(self.size)

    def delete_kth_index(self, k):
        if k > self.size:
            raise IndexError('List Index out of range')
        else:
            self.arr[k], self.arr[-1] = self.arr[-1], self.arr[k]
            self.arr.pop()
            self.size -= 1
            self.percolate_down(k)


if __name__ == "__main__":
    heap = Heap()
    nums = [12, 32, 43, 95, 30]
    [heap.append(num) for num in nums]
    heap.delete_kth_index(3)
    print(heap.arr[1:])
