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

    @staticmethod
    def insert_level_order(root, data):
        newNode = Node(data)
        if root is None:
            root = newNode
            return root
        else:
            arr = [root]
            while arr:
                node = arr.pop()

                if node.data == data:
                    return root

                if node.left_child is not None:
                    arr.append(node.left_child)
                else:
                    node.left_child = newNode
                    return root

                if node.right_child is not None:
                    arr.append(node.right_child)
                else:
                    node.right_child = newNode
                    return root

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
    [tree.insert_level_order(tree.root_node, num) for num in nums]

    print(tree.preorder_traversal(tree.root_node, []))

