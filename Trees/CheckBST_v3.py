class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root_node = None

    def check_binary(self, root):
        if root is None:
            return True
        else:
            if root.left and root.left.data > root.data:
                return False
            if root.right and root.right.data < root.data:
                return False
            if not self.check_binary(root.left) or not self.check_binary(root.right):
                return False

        return True

    def inorder_traversal(self, root, arr):
        if root is None:
            return
        else:
            self.inorder_traversal(root.left, arr)
            arr.append(root.data)
            self.inorder_traversal(root.right, arr)

        return arr


if __name__ == "__main__":
    tree = Tree()
    
    print(tree.check_binary(tree.root_node))
