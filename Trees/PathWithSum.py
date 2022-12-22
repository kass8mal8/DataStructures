""" Give an algorithm for checking the existence of path with given sum. That means, given a sum,
check whether there exists a path from root to any of the nodes. """


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

    def find_path(self, root, val, path, paths):
        if not root:
            return
        if not root.left_child and not root.right_child:
            if root.data == val:
                path.append(root.data)
                paths.append(path)
                return True
            else:
                return False

        self.find_path(root.left_child, val - root.data, path + [root.data], paths)
        self.find_path(root.right_child, val - root.data, path + [root.data], paths)

    def has_path_sum(self, root, val):
        paths = []
        self.find_path(root, val, paths, [])
        print(f"Path: {paths}")

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
    nums = [17, 29, 13, 43, 23, 74]
    [tree.insert(num) for num in nums]

    print(tree.inorder_traversal(tree.root_node, []))
    tree.has_path_sum(tree.root_node, 30)
