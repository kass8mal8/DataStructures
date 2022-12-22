""" Algorithm to find if a string is palindrome using Stack ADT """


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        top = self.items.pop()
        return top


if __name__ == "__main__":
    stack = Stack()

    def is_palindrome(word):
        isPalindrome = False
        for x in word:
            stack.push(x)
            
        for w in word:
            if w == stack.pop():
                isPalindrome = True
            else:
                isPalindrome = False

        return isPalindrome

    statement = 'madam'
    print(is_palindrome(statement))
