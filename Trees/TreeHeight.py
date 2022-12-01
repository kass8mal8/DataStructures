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

    def inorder(self, root, arr):
        if root is None:
            return
        else:
            arr.append(root.data)
            self.inorder(root.left_child, arr)
            self.inorder(root.right_child, arr)
        return arr


if __name__ == "__main__":
    tree = Tree()
    nums = [23, 21, 20, 32, 19]
    [tree.insert(num) for num in nums]
    print(tree.inorder(tree.root_node, []))


