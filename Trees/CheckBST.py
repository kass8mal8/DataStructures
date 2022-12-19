""" Give an algorithm to check whether the given binary tree is a BST or not. """


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
    nums = [13, 28, 32, 84]
    [tree.insert(num) for num in nums]

    if tree.check_binary(tree.root_node):
        print('A Binary Search Tree')
    else:
        print('Not Binary Search Tree')
