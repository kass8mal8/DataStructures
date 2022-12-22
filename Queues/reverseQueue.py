""" Give an algorithm for reversing a queue Q. To access the queue, we are only allowed to use the
methods of queue ADT. """


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, data):
        self.inStack.push(data)

    def dequeue(self):
        if not self.outStack.items:
            while self.inStack.items:
                self.outStack.push(self.inStack.pop())

        return self.outStack.pop()


if __name__ == "__main__":
    Q = Queue()
    nums = [15, 19, 12, 18, 23]
    [Q.enqueue(num) for num in nums]
