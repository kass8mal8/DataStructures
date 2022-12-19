class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.next_sibling = None


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

    def fill_sibling_pointer(self, root):
        if root is None:
            return
        else:
            if root.left_child:
                root.left.next_sibling = root.right
            if root.right_child:
                if root.next_sibling:
                    root.right_child.next_sibling = root.left_child
                else:
                    root.right_child.next_sibling = None

        self.fill_sibling_pointer(root.left_child)
        self.fill_sibling_pointer(root.right_child)


if __name__ == "__main__":
    tree = Tree()
    nums = [12, 23, 43, 40, 29]

    [tree.insert(num) for num in nums]
    tree.fill_sibling_pointer(tree.root_node)
