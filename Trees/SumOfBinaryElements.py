""" Give an algorithm for finding the sum of all elements in binary tree. """


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

    def sum_binary_tree(self, root):
        if root is None:
            return 0
        else:
            return root.data + self.sum_binary_tree(root.left_child) + self.sum_binary_tree(root.right_child)


if __name__ == "__main__":
    tree = Tree()
    nums = [10, 32, 29, 19, 36]
    [tree.insert(num) for num in nums]

    print(f"Sum: {tree.sum_binary_tree(tree.root_node)}")
