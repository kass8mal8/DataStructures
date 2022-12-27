""" Given a binary tree, how do you remove its leaves? """


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

    def remove_leaves(self, root):
        if not root:
            return
        if root.left_child is None and root.right_child is None:
            return None
        else:
            root.left = self.remove_leaves(root.left_child)
            root.right = self.remove_leaves(root.right_child)

        return root

    def inorder_traversal(self, root, arr):
        if root is None:
            return
        else:
            self.inorder_traversal(root.left_child, arr)
            arr.append(root.data)
            self.inorder_traversal(root.right_child, arr)

        return arr


if __name__ == "__main__":
    tree = Tree()
    nums = [17, 29, 13, 43, 23, 74, 15, 14, 16, 6]
    [tree.insert(num) for num in nums]

    print(tree.inorder_traversal(tree.root_node, []))
    tree.remove_leaves(tree.root_node)
    print(tree.inorder_traversal(tree.root_node, []))
