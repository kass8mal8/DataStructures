""" Algorithm to delete nth node from the end of a linked list """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        current, node = self.head, Node(data)

        if self.head is None:
            self.head = node
            return
        else:
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
            
    def deleteNth(self, n):
        if 0 > n > self.size:
            raise Exception("List index out of range")
        else:
            count, current = 0, self.head
            while count < self.size - n:
                count += 1
                current = current.next

            current.next = current.next.next


if __name__ == "__main__":
    L = LinkedList()
    nums = [10, 17, 28, 21]

    [L.append(num) for num in nums]
    print([num for num in L.iter()])
    L.deleteNth(3)
    print([num for num in L.iter()])
