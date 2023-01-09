""" Give an algorithm to find sum of first K elements """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return
        else:
            current = self.root_node
            parent = None

            while True:
                parent = current

                if current.data < node.data:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

                else:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return

    @staticmethod
    def sum_first_k(root, k):
        if root is None:
            return 0
        else:
            arr = [root]
            count, total = 0, 0

            while arr and count < k:
                node = arr.pop()
                count += 1
                total += node.data

                if node.left_child:
                    arr.append(node.left_child)
                if node.right_child:
                    arr.append(node.right_child)

        return total


if __name__ == "__main__":
    tree = Tree()
    nums = [10, 32, 29, 19, 36]
    [tree.insert(num) for num in nums]

    print(f"Sum: {tree.sum_first_k(tree.root_node, 4)}")
