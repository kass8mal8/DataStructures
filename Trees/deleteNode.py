""" Give an algorithm for deleting an e lement (assuming dala is given) from binary tree."""

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

    def post_order(self, root, arr):
        if root is None:
            return
        else:
            self.post_order(root.left_child, arr)
            self.post_order(root.right_child, arr)
            arr.append(root.data)

        return arr

    def search_node(self, data):
        # search tree and find node to be deleted
        current = self.root_node
        if current.data < data:
            current = current.left_child
            while current.data != data:
                current = current.left_child
                if current.data == data:
                    return current.data

        else:
            current = current.right_child
            while current.data != data:
                current = current.right_child
                if current.data == data:
                    return current.data


if __name__ == "__main__":
    tree = Tree()
    nums = [18, 21, 10, 14, 23, 7, 13, 3]
    [tree.insert(num) for num in nums]
    print(f"Tree:{[num for num in tree.post_order(tree.root_node, [])]}")
    print(f"Data:{tree.search_node(18)}")
