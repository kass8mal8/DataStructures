""" Algorithm to check if BT is a BST
    Time complexity for this algorithm is O(n) """

# You need to have tree data I've skipped insertion fo tree data


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def check_binary(self, root, minimum, maximum):
        if root is None:
            return True
        else:
            if root.data <= minimum or root.data >= maximum:
                return False  # root node must be greater than min and less than max
            result = self.check_binary(root.left_child, minimum, root.data)
            result = result and self.check_binary(root.right_child, root.data, maximum)

            return result


if __name__ == "__main__":
    tree = Tree()

    if tree.check_binary(tree.root_node, float("-infinity"), float("infinity")):
        print('A Binary Search Tree')
    else:
        print('Not Binary Search Tree')
