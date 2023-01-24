""" Algorithm to find height of a node """


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

    def inorder_traversal(self, root, arr):
        if not root:
            return
        else:
            self.inorder_traversal(root.left_child, arr)
            arr.append(root.data)
            self.inorder_traversal(root.right_child, arr)

        return arr

    def height(self, root, x):
        if root is None:
            return 0
        else:
            left = self.height(root.left_child, x)
            right = self.height(root.right_child, x)

            ans = max(left, right) + 1

            if root.data == x:
                return ans


if __name__ == "__main__":
    tree = Tree()
    nums = [13, 21, 76, 38, 29]

    [tree.insert(num) for num in nums]
    print(tree.inorder_traversal(tree.root_node, []))
    print(f"Height:{tree.height(tree.root_node, 76)}")
