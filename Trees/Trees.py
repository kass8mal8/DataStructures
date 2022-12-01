class Node:
    def __init__(self, data=None):
        self.left_child = None
        self.right_child = None
        self.data = data


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

    def preorder_traversal(self, root_node, array):
        if root_node is None:
            return
        else:
            self.preorder_traversal(root_node.left_child, array)
            array.append(root_node.data)
            self.preorder_traversal(root_node.right_child, array)

        return array

    def print_tree(self):
        print(f"Values of Tree:{self.preorder_traversal(tree.root_node, [])}")

    def find_min(self):
        current = self.root_node
        if current is None:
            return
        else:
            while current.left_child:
                current = current.left_child

            return current.data

    def find_max(self):
        current = self.root_node
        if current is None:
            return
        else:
            while current.right_child:
                current = current.right_child

            return current.data

    def find_node(self, root_node, data):
        if root_node is None:
            return False
        array = list()
        array.append(root_node)
        node = None

        while array:
            node = array.pop()
            if node.data == data:
                return node.data
            if root_node.left_child is not None:
                array.append(root_node.left_child)
            if root_node.right_child is not None:
                array.append(root_node.right_child)


if __name__ == "__main__":
    tree = Tree()
    nums = [23, 11, 10, 9, 32]
    [tree.append(num) for num in nums]
    tree.print_tree()
    print(f"Minimum value:{tree.find_min()}")
    print(f"Maximum value:{tree.find_max()}")
    print(f"{tree.find_node(tree.root_node, 11)}")
