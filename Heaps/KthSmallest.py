""" Give an algorithm for finding the kth smallest element in min-heap. """


class Heap:  # Min Heap
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

            if self.heapArr[i] > self.heapArr[index]:
                self.heapArr[i], self.heapArr[index] = self.heapArr[index], self.heapArr[i]

            i = index

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heapArr[i] < self.heapArr[i // 2]:
                self.heapArr[i], self.heapArr[i // 2] = self.heapArr[i // 2], self.heapArr[i]

            i //= 2

    def delete_min(self):
        self.heapArr[1], self.heapArr[-1] = self.heapArr[-1], self.heapArr[-1]
        self.size -= 1
        return self.heapArr.pop()

    def insert(self, data):
        self.heapArr.append(data)
        self.size += 1
        self.percolate_up(self.size)

    def right_child(self, i):
        if i * 2 + 1 <= self.size:
            return self.heapArr[i * 2 + 1]
        return -1

    def left_child(self, i):
        if i * 2 <= self.size:
            return self.heapArr[i * 2]
        return -1

    def search_element(self, itm):
        i = 1
        while i <= self.size:
            if itm == self.heapArr[i]:
                return i
            i += 1


if __name__ == "__main__":
    HOrig = Heap()
    nums = [12, 13, 19,5, 7]
    [HOrig.insert(nm) for nm in nums]

    def kth_smallest(OrigHeap, k):
        count, HAux = 1, Heap()
        item = OrigHeap.heapArr[1]
        HAux.insert(item)

        if count == k:
            return item

        while HAux.size >= 1:
            item = HAux.delete_min()
            count += 1

            if count == k:
                return item
            else:
                if OrigHeap.right_child(OrigHeap.search_element(item)) != -1:
                    HAux.insert(OrigHeap.right_child(OrigHeap.search_element(item)))

                if OrigHeap.left_child(OrigHeap.search_element(item)) != -1:
                    HAux.insert(OrigHeap.right_child(OrigHeap.search_element(item)))

    print(kth_smallest(HOrig, 3))
    print(HOrig.heapArr[1:])
