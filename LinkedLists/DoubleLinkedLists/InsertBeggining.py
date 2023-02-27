""" Algorithm to insert a node on the beginning of a double linkedlist """


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_beginning(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return
        else:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def traverse(self):
        current = self.head

        while current:
            print(current.data, " ")
            current = current.next


if __name__ == "__main__":
    DL = DLinkedList()
    nums = [19, 29, 34, 12]

    [DL.insert_beginning(num) for num in nums]
    DL.traverse()
