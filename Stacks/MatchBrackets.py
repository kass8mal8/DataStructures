""" Algorithm that matches brackets from a string """


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.insert(0, data)

    def pop(self):
        return self.items.pop(0)

    def isEmpty(self):
        return True if len(self.items) == 0 else False


if __name__ == "__main__":

    def isMatched(expr):

        left = ['(', '{', '[']  # opening delimiters
        right = [')', '}', ']']  # respective closing delims

        S = Stack()

        for c in expr:
            if c in left:
                S.push(c)  # push left delimiter on stack
            elif c in right:
                if S.isEmpty(): return False  # nothing to match with

                if right.index(c) != left.index(S.pop()):
                    return False  # mismatched

                return S.isEmpty()

    expression = "[Hello world]"
    print(isMatched(expression))
