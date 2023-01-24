""" Write a program that takes as input the root of a binary tree and checks whether the tree is Height Balanced. """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def append(self, data):
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

    def preorder_traversal(self, root, arr):
        if root is None:
            return
        else:
            arr.append(root.data)
            self.preorder_traversal(root.left_child, arr)
            self.preorder_traversal(root.right_child, arr)

        return arr

    def isBalanced(self, root):
        if not root:
            return 0
        else:
            left = self.isBalanced(root.left_child) + 1
            right = self.isBalanced(root.right_child) + 1

            ans = abs(left - right)
            return True if ans <= 1 else False


if __name__ == "__main__":
    tree = Tree()
    nums = [13, 21, 39, 28, 7, 11, 15]

    [tree.append(num) for num in nums]
    print(f"Tree:{tree.preorder_traversal(tree.root_node, [])}")

    print(tree.isBalanced(tree.root_node))
