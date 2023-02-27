""" Algorithm to delete last element from a doubly linkedlist """


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
        if not self.head:
            self.head = Node(data, None, None)
            return
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = Node(data, None, current)

        self.size += 1

    def remove_last(self):
        current = self.head
        previous = self.head

        while current.next:
            previous = current
            current = current.next

        print(f"\nRemoved element: {previous.next.data}")
        previous.next = None

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


if __name__ == "__main__":
    DL = DLinkedList()
    nums = [19, 23, 10, 27]

    [DL.append(num) for num in nums]
    print(f"--- Original LinkedList --- \n{[num for num in DL.iter()]}")
    DL.remove_last()
    print(f"\n--- LinkedList After --- \n{[num for num in DL.iter()]}")
