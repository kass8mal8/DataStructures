""" Algorithm to return Nth element from the end """


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


class DLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = Node(data, None, current)

        self.size += 1

    def nth_node(self, n):
        current, count = self.head, 0

        while count < self.size - n:
            count += 1
            current = current.next

        return current.next.data

    def iter(self):
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val


if __name__ == "__main__":
    DL = DLinkedList()
    nums = [19, 27, 18, 23]

    [DL.append(num) for num in nums]
    print([num for num in DL.iter()])

    x = 1
    print(f"Node {x} from last:{DL.nth_node(x)}")
