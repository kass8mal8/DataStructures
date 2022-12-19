class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.insert(0, data)

    def pop(self):
        return self.items.pop()


if __name__ == "__main__":
    def match_brackets(statement):
        stack = Stack()
        isBalanced = False

        for word in statement:
            if word in ["{", "[", "("]:
                stack.push(word)

        top = stack.pop()

        while stack.items:
            for w in statement:
                if w == "}" or w == "]" or w == ")" and w == top:
                    isBalanced = True
                else:
                    isBalanced = False
                top = stack.pop()

            return "Brackets Match" if isBalanced else "Brackets don't match"


    print(match_brackets("Hello ()"))
