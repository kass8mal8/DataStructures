""" Algorithm to find Max using recursion """


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

        if not self.root_node:
            self.root_node = node
            return
        else:
            current = self.root_node
            while True:
                parent = current

                if current.data > node.data:
                    current = current.left_child
                    if not current:
                        parent.left_child = node
                        return

                else:
                    current = current.right_child
                    if not current:
                        parent.right_child = node
                        return

    def max_recursive(self, root):
        # current = root
        if root.right_child is None:
            return root.data
        else:
            return self.max_recursive(root.right_child)

    def preorder_traversal(self, root, arr):
        if not root:
            return
        else:
            arr.append(root.data)
            self.preorder_traversal(root.left_child, arr)
            self.preorder_traversal(root.right_child, arr)

        return arr


if __name__ == "__main__":
    tree = Tree()
    nums = [23, 21, 27, 18, 22, 24, 29]
    [tree.insert(num) for num in nums]

    print(tree.preorder_traversal(tree.root_node, []))
    print(f"Maximum: {tree.max_recursive(tree.root_node)}")
