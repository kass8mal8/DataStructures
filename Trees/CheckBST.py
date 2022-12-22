""" Give an algorithm to check whether the given binary tree is a BST or not. """
# Time complexity for this algorithm is O(n^2)


class Tree:
    def __init__(self):
        self.root_node = None

    # find maximum
    def find_max(self, root):
        if root.right_child is None:
            return root.data
        else:
            return self.find_max(root.left_child)

    # find minimum
    def find_min(self, root):
        if root.left_child is None:
            return root.data
        else:
            return self.find_min(root.right_child)

    def check_binary(self, root):
        if root is None:
            return True
        else:
            # compare left node with its maximum
            if root.left_child and self.find_max(root.left_child) > root.data:
                return False

            # compare right node with its minimum
            if root.right_child and self.find_min(root.right_child) < root.data:
                return False

            # compare the entire tree
            if not self.check_binary(root.left_child) or not self.check_binary(root.right_child):
                return False

            return True


if __name__ == "__main__":
    tree = Tree()

    if tree.check_binary(tree.root_node):
        print('A Binary Search Tree')
    else:
        print('Not Binary Search Tree')
