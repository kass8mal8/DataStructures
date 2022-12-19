class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.insert(0, data)

    def pop(self):
        self.items.pop()


if __name__ == "__main__":
    stack = Stack()
    nums = [12, 10, 23, 39]
    [stack.push(nm) for nm in nums]

    print(stack.items)