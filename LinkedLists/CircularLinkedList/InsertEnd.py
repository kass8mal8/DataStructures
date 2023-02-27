""" Algorithm to insert a node at end of a circular linkedlist """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        current, node = self.head, Node(data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            current.next = node

        while current.next != self.head:
            current = current.next

        # node.next = node

    def iter(self):
        current = self.head

        while current != self.head:
            val = current.data
            current = current.data
            yield val


if __name__ == "__main__":
    CL = CLinkedList()
    nums = [91, 71, 28, 10]

    [CL.append(num) for num in nums]
    print([num for num in CL.iter()])
