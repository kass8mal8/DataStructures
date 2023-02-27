""" Algorithm to count nodes in a Circular linkedlist """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CLinkedList:
    def __init__(self):
        self.head = None

    def count_nodes(self):
        current = self.head

        if current is None:
            return 0

        count, current = 1, current.next

        while current != self.head:
            current = current.next
            count += 1

        return count

