class Stack:
    def __init__(self, limit=5):
        self.limit = limit
        self.items = limit * [None]

    def size(self):
        return len(self.items) > 0

    def push(self, data):
        self.items.append(data)

    def resize(self):
        if len(self.items) > self.limit:
            new_items = list(self.items)
            self.limit = 2 * self.limit
            self.items = new_items


if __name__ == "__main__":
    stack = Stack()
    nums = [12, 39, 46]
    [stack.push(num) for num in nums]
    print(stack.items)
