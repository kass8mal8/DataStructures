""" write an algorithm to find depth of a BT """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        if not self.root_node:
            self.root_node = Node(data)
            return
        else:
            current, node = self.root_node, Node(data)

            while True:
                parent = current

                if current.data[0] > node.data[0]:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def inorder_traversal(self, root, arr):
        if not root:
            return
        else:
            self.inorder_traversal(root.left_child, arr)
            arr.append(root.data)
            self.inorder_traversal(root.right_child, arr)

        return arr

    def depth_tree(self, root):
        if root is None:
            return 0
        else:
            return max(self.depth_tree(root.left_child), self.depth_tree(root.right_child)) + 1


if __name__ == "__main__":
    tree = Tree()
    media = [(13, "school"), (10, "Girl Friend"), (21, "Lucid Dreams"), (17, "East Side")]
    [tree.insert(m) for m in media]
    print(tree.inorder_traversal(tree.root_node, []))
    print(f"Depth:{tree.depth_tree(tree.root_node)}")
