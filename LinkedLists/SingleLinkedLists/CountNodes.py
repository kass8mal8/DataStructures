""" Give an algorithm to count the number of nodes in a linkedlist recursively """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        current = self.head

        if self.head is None:
            self.head = node
            return
        else:
            while current.next:
                current = current.next

            current.next = node

    def countNodes(self):
        current, count = self.head, 0
        while current:
            count += 1
            current = current.next

        return f"Number of nodes:{count}"

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


if __name__ == "__main__":
    L = LinkedList()
    nums = [10, 19, 23, 42, 91]

    [L.insert(num) for num in nums]
    print([num for num in L.iter()])
    print(L.countNodes())
