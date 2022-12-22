""" Given an integer k and a queue of integers, how do you reverse the order of the first k elements
of the queue, leaving the other elements in the same relative order? For example, if k=4 and queue has the
elements (10, 20, 30, 40, 50, 60, 70, 80, 90); the output should be [40, 30, 20, 10, 50, 60, 70, 80, 90]. """


# construct Queue
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)


if __name__ == "__main__":
    q = Queue()
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    [q.enqueue(num) for num in nums]
    num = 4

    def rev_first_k(k, queue):
        stack = []

        for x in range(k):
            stack.append(queue.dequeue())

        while stack:
            queue.enqueue(stack.pop())

        for x in range(0, len(queue.items) - k):
            queue.enqueue(queue.dequeue())

        return queue.items


    result = rev_first_k(num, q)
    print(result)
