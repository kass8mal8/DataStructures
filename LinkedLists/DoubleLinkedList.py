class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data, None, None)

        if self.head is None:
            self.head = node
            self.tail = self.head

        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = Node(data, None, current)
            self.size += 1

    def insert_first(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_at(self, index, data):
        if self.size < index < 0:
            raise Exception("List index out of range:")
        elif self.head is None or index == 0:
            self.insert_first(data)
        elif index == self.size:
            self.append(data)
        else:
            count = 0
            current = self.head

            while count < index - 1 and current.next:
                count += 1
                current = current.next
            current.next = Node(data, current.next, current)
        self.size += 1

    def remove_at(self, index):
        if index == 0 and self.head is not None:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size:
            current = self.head
            previous = self.head

            if self.head is None:
                return
            else:
                while current.next:
                    previous = current
                    current = current.next

                previous.next = None
                self.size -= 1

        else:
            count = 0
            current = self.head

            while count < index - 1:
                count += 1
                current = current.next

            current.next = current.next.next
            self.size -= 1

    def iter(self):
        current = self.head

        while current:
            val = current.data
            current = current.next

            yield val


double = DoublyLinkedList()

[double.append(x) for x in ['Lisa', 'Elsie', 3, 8]]
double.remove_at(2)
print([name for name in double.iter()])
