class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class L1:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        current = self.head
        if self.head is None:
            self.head = node
            return
        else:
            while current.next:
                current = current.next

            current.next = node
        self.size += 1


class L2:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        current = self.head
        if self.head is None:
            self.head = node
            return
        else:
            while current.next:
                current = current.next

            current.next = node
        self.size += 1


class Solution:
    def __init__(self, list_one, list_two):
        self.one = list_one
        self.two = list_two

    def append(self, data):
        dummy = Node(data)

        while self.one and self.two:
            if self.one.data < self.two.data:
                self.one.append(self.two.data)
            else:
                self.two.append(self.one.data)


l_one = L1()
l_two = L2()

nums = [1, 3, 5, 8]
numbers = [9, 4, 11, 25]

[l_one.append(num) for num in nums]
[l_two.append(num) for num in numbers]

sltn = Solution()
sltn.append()
