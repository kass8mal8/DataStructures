""" Give an algorithm for finding the size of a BST """


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
        else:
            current = self.root_node
            while True:
                parent = current
                if current.data > node.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def size_tree(self, root):
        if root is None:
            return 0
        else:
            return self.size_tree(root.left_child) + self.size_tree(root.right_child) + 1


if __name__ == "__main__":
    tree = Tree()
    nums = [23, 43, 39, 2, 37]
    [tree.insert(num) for num in nums]
    print(f"Size of Tree: {tree.size_tree(tree.root_node)}")
