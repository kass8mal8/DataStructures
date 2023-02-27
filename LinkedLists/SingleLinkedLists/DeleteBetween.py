class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Insert Algorithm
    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node
        self.size += 1

    # Algorithm to delete node between two nodes
    def delete_btwn(self, index):
        if self.head is None:
            return
        else:
            current, count = self.head, 0

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


if __name__ == "__main__":
    L = LinkedList()
    nums = [23, 29, 43, 19]

    [L.insert_end(num) for num in nums]
    print(f"Before Deleting:{[num for num in L.iter()]}")
    L.delete_btwn(2)
    print(f"After Deleting:{[num for num in L.iter()]}")
