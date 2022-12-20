""" Give a n a lgorithm for findin g the clccpcst node of the binary tree.  """


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

    def deep_node(self, root):
        if root is None:
            return
        else:
            arr = [root]
            node = None

            while arr:
                node = arr.pop()
                if node.left_child:
                    arr.append(node.left_child)
                if node.right_child:
                    arr.append(node.right_child)

            return node.data

    def post_order(self, root, arr):
        if root is None:
            return
        else:
            self.post_order(root.left_child, arr)
            self.post_order(root.right_child, arr)
            arr.append(root.data)

        return arr


if __name__ == "__main__":
    tree = Tree()
    nums = [18, 21, 10, 14, 23, 7, 13, 3]
    [tree.insert(num) for num in nums]
    print(f"Tree:{[num for num in tree.post_order(tree.root_node, [])]}")
    print(f"Deepest node:{tree.deep_node(tree.root_node)}")
