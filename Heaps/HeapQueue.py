""" How do we implement a Queue using heap? """


class Heap:
    def __init__(self):  # min heap
        self.heapArr = [0]
        self.size = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heapArr[i] < self.heapArr[i // 2]:
                self.heapArr[i], self.heapArr[i // 2] = self.heapArr[i // 2], self.heapArr[i]

            i //= 2

    def append(self, data):
        self.heapArr.append(data)
        self.size += 1
        self.percolate_up(self.size)

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

    def delete_min(self):
        self.heapArr[1], self.heapArr[-1] = self.heapArr[-1], self.heapArr[1]
        self.size -= 1
        itm = self.heapArr.pop()
        self.percolate_down(1)
        return itm


class Queue:
    def __init__(self):
        self.items = Heap()

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.delete_min()


if __name__ == "__main__":
    q = Queue()
    nums = [13, 11, 23, 18]
    [q.push(num) for num in nums]

    print(f"Queue: {q.items.heapArr[1:]}")
    print(q.pop())

