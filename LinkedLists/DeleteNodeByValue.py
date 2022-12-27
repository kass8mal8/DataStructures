""" Algorithm to delete a node by given value from the linkedlist
"""


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

    # search for the data in linkedlist then delete it
    def delete_by_data(self, data):
        current, previous = self.head, self.head

        while current:
            if current.data == data:
                previous.next = current.next
                self.size -= 1
                return
            else:
                previous, current = current, current.next
        print(f"{data} not found in list")

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
    L.delete_by_data(27)
    print(f"After Deleting:{[num for num in L.iter()]}")
