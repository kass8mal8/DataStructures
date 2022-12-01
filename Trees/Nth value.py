class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def nth_node_from_last(self, n):
        current = self.head
        size = 0
        if self.head is None:
            return
        while current:
            size += 1
            current = current.next

        current = self.head

        count = 0
        while count < size - n:
            count += 1
            current = current.next

        return current.data

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


linkedlist = LinkedList()
nums = [3, 4, 12, 30, 19]

[linkedlist.insert_first(num) for num in nums]
print([num for num in linkedlist.iter()])
x = 2
print(f"{x}nd node from the last:{linkedlist.nth_node_from_last(x)}")
