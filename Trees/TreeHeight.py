class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    # add new elements to the BST
    def insert(self, data):
        node = Node(data)

        if self.root_node is None:
            self.root_node = node
            return
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

    # find Height of the BST
    def height(self, root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left_child), self.height(root.right_child)) + 1


if __name__ == "__main__":
    tree = Tree()
    nums = [23, 26, 20, 32, 19]
    [tree.insert(num) for num in nums]
    print(f"Height of Tree: {tree.height(tree.root_node)}")
