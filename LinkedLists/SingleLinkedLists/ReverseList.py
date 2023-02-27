""" Reverse a singly linked list. """


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

    def reverse(self):
        last = None
        current = self.head

        while current:
            next_node = current.next
            current.next = last
            last = current
            current = next_node

        self.head = last

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


if __name__ == "__main__":
    L = LinkedList()
    nums = [23, 29, 43, 19]
    [L.insert_beginning(num) for num in nums]

    print(f"Before reversing:{[num for num in L.iter()]}")
    L.reverse()
    print(f"After reversing:{[num for num in L.iter()]}")
