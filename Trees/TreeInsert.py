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

    def inorder(self, root, arr):
        if not root:
            return
        else:
            self.inorder(root.left_child, arr)
            arr.append(root.data)
            self.inorder(root.right_child, arr)

        return arr


if __name__ == "__main__":
    tree = Tree()
    nums = [13, 32, 39, 20, 43]

    [tree.insert(num) for num in nums]
    print(tree.inorder(tree.root_node, []))

