"""Queue implementation using linked lists"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None

    def enqueue(self, data):
        current = self.head
        node = Node(data)

        if self.head is None:
            self.head = node
            return
        else:
            while current.next:
                current = current.next

            current.next = node

    def dequeue(self):
        if self.head is None:
            print("Sorry the queue is empty")
        else:
            return self.head.data

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


queue = Queue()

[queue.enqueue(x) for x in ['AlgoExpert', 'LeetCode', 'Hackerrank']]
print([plat for plat in queue.iter()])
print(queue.dequeue())
