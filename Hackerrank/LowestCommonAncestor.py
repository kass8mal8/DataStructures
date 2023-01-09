""" You are given a pointer to the root of a BST and two values v1 and v2.You need to return the lowest common ancestor LCA of v1 and v2 in the BST """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None
        self.size = 0

    def lca(self, root, v1, v2):
        if root is None:
            return -1
        if root == v1 and root == v2:
            return root.data
        else:
            left, right = self.lca(root.left_child, v1, v2), self.lca(root.right_child, v1, v2)

            if left and right:
                return root.data
            else:
                return left if left else right
