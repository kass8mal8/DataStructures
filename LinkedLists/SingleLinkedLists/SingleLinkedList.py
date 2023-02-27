class Node:
    def __init__(self, data=None) -> None:
        self.next = None
        self.data = data


class SingleLinkedList:
    def __init__(self) -> None:
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

    def nth_node_from_last(self, index):
        if self.head is None:
            return
        else:
            current = self.head
            count = 0

            while count < self.size - index:
                count += 1
                current = current.next

            return current.next.data

    def remove_nth_node_from_last(self, index):
        if self.head is None:
            return
        else:
            current = self.head
            count = 0

            while count < self.size - index:
                count += 1
                current = current.next

            current.next = current.next.next

    def reverse_linked_list(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


linkedlist = SingleLinkedList()
nums = [51, 97, 61, 73]
[linkedlist.append(num) for num in nums]
linkedlist.remove_nth_node_from_last(1)
print([num for num in linkedlist.iter()])
