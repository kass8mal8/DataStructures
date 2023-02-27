""" Remove duplicate """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = Node(data)

        self.size += 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


if __name__ == "__main__":
    L = LinkedList()
    nums = [10, 10, 19, 21, 21, 21, 28]

    [L.append(num) for num in nums]
    A = [num for num in L.iter()]

    print(A)
