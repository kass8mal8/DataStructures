""" Give an algorithm for finding the number of leaves in the binary tree without using recursion. """


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
                if current.data < node.data:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return
                else:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return

    @staticmethod
    def leaf_number(root):
        if root is None:
            return
        else:
            arr = [root]
            node = None
            count = 0

            while arr:
                node = arr.pop()

                if node.left_child is None and node.right_child is None:
                    count += 1

                else:
                    if node.left_child:
                        arr.append(node.left_child)
                    if node.right_child:
                        arr.append(node.right_child)

            return count

    def preorder_traversal(self, root, arr):
        if root is None:
            return
        else:
            arr.append(root.data)
            self.preorder_traversal(root.left_child, arr)
            self.preorder_traversal(root.right_child, arr)

        return arr


if __name__ == "__main__":
    tree = Tree()
    nums = [12, 19, 21, 10, 28, 32]
    [tree.insert(num) for num in nums]

    print(tree.preorder_traversal(tree.root_node, []))
    print(f"Leaf Nodes: {tree.leaf_number(tree.root_node)}")
