""" Given a binary tree, how do you remove its leaves? """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def remove_leaves(self, root):
        if not root:
            return
        if root.left_child is None and root.right_child is None:
            return None
        else:
            root.left = self.remove_leaves(root.left_child)
            root.right = self.remove_leaves(root.right_child)

        return root


