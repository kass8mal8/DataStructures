class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, data):
        self.items.append(data)
        self.size += 1

    def pop(self):
        return self.items.pop(0)


if __name__ == "__main__":
    stack = Stack()

    def match(tp, bt):
        if tp == "{" and bt == "}" or tp == "[" and bt == "]" or tp == "(" and bt == ")":
            return "Symbols match"
        else:
            return False


    def balance_symbols(statement):
        for st in statement:
            if st in ["{", "[", "("]:
                stack.push(st)

            if st in ["}", "]", ")"]:
                length = len(stack.items)
                top = stack.pop()
                arr = [st]

                if len(arr) == length:
                    match(top, st)
                else:
                    return "Symbols dont match"


    symbols = "{}"
    print(balance_symbols(symbols))
