""" Algorithm to insert data between two nodes of a linkedlist
    time complexity O(n) """


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

    def insert_btwn(self, index, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current, count = self.head, 0

            while count < index - 1:
                count += 1
                current = current.next

            node.next = current.next
            current.next = node

        self.size += 1

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

    print(f"Before Inserting:{[num for num in L.iter()]}")
    L.insert_btwn(2, 32)
    print(f"After inserting at index 2:{[num for num in L.iter()]}")
