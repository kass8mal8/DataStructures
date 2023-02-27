""" Implement a stack using linked lists """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
            return
        else:
            node.next, self.top = self.top, node
        self.size += 1

    def pop(self):
        if self.top is None:
            return
        else:
            current = self.top
            previous = self.top

            while current.next:
                previous, current = current, current.next

            previous.next = None
            return current.data

    def iter(self):
        current = self.top
        while current:
            val = current.data
            current = current.next
            yield val


if __name__ == "__main__":
    stack = Stack()
    nums = [12, 16, 21, 28, 31, 35, 43]
    [stack.push(num) for num in nums]
    print([num for num in stack.iter()])
    print(stack.pop())
