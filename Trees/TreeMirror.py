""" Given two trees, give an algorithm for checking whether they are mirrors of each other. """
from TreeSize import Tree as Tr
from Trees import Tree as TT


def are_mirrors(root1, root2):
    if not root1 and not root2:
        return True
    if root1.data != root2.data:
        return False
    else:
        return are_mirrors(root1.left_child, root2.right_child) and are_mirrors(root1.right_child, root2.left_child)


check = are_mirrors(Tr, TT)
print(check)
