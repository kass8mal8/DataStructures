""" Algorithm to insert data to the head of a linkedlist
    time complexity O(1) """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_beginning(self, data):
        node = Node(data)
        node.next, self.head = self.head, node

        self.size += 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


if __name__ == "__main__":
    L = LinkedList()
    nums = [13, 27, 15, 10]
    [L.insert_beginning(num) for num in nums]
    print([num for num in L.iter()])
