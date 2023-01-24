""" Binary Tree implementation """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.root_node = None

    def insert_left(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
            return
        else:
            current, node = self.root_node, Node(data)
            node.left_child, current.left_child = current.left_child, node

    def insert_right(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
            return
        else:
            current, node = self.root_node, Node(data)
            node.right_child, current.right_child = current.right_child, node

    def preorder_traversal(self, root, arr):
        if root is None:
            return
        else:
            arr.append(root.data)
            self.preorder_traversal(root.left_child, arr)
            self.preorder_traversal(root.right_child, arr)

        return arr


if __name__ == "__main__":
    tree = BinaryTree()
    nums = [12, 23, 28, 9, 19, 32]
    [tree.insert_left(num) for num in nums]

    print(tree.preorder_traversal(tree.root_node, []))

