class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.insert(0, data)

    def pop(self):
        return self.items.pop()


if __name__ == "__main__":
    stack = Stack()
    nums = [13, 17, 10, 31, 27]

    [stack.push(num) for num in nums]
    print(stack.items)

    while stack.items:
        print(stack.pop())
