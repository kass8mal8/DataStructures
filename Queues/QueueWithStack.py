""" How can you implement a queue using two stacks """


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) < 1


class Queue:
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()

    def enqueue(self, data):
        self.st1.push(data)

    def dequeue(self):
        if not self.st2.items:
            while self.st1.items:
                self.st2.push(self.st1.pop())

        arr = []
        while self.st2.items:
            arr.append(self.st2.pop())

        return arr


if __name__ == "__main__":
    q = Queue()
    nums = [13, 29, 32, 10]
    [q.enqueue(num) for num in nums]

    print(q.dequeue())
