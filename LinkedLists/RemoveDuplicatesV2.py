""" Code to remove duplicates from a linked list  """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

        self.size += 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    @staticmethod
    def removeDuplicates(root):
        if root is None:
            return
        else:
            current = root
            while current.next:
                current = current.next
                if current.next == current:
                    current.next = current.next.next


if __name__ == "__main__":
    L = LinkedList()
    nums = [4, 7, 7, 11, 11, 11, 19, 28, 28]
    [L.append(num) for num in nums]

    print([num for num in L.iter()])
    L.removeDuplicates(L.head)
    print([num for num in L.iter()])
