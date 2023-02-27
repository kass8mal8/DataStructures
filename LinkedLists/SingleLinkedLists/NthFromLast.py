""" Find nth node from end of a linkedlist using two scans """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

    def nth_from_last(self, index):
        # find size of linkedlist
        size, count, current = 0, 0, self.head

        while current:
            current = current.next
            size += 1

        current = self.head

        # iterate the linkedlist
        while count < size - index:
            count += 1
            current = current.next

        return current.data

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


if __name__ == "__main__":
    linkedlist = LinkedList()
    nums = ['movies', 32, 'books', 'games', 11, 27]
    [linkedlist.append(num) for num in nums]
    print([num for num in linkedlist.iter()])
    print(linkedlist.nth_from_last(3))
