""" Give an algorithm for printing the level order data in reverse order. """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


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
                    current = current.left
                    if current is None:
                        parent.left = node
                        return

                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return

    @staticmethod
    def print_reverse(root):
        if root is None:
            raise Exception("Tree is empty")
        else:
            arr = [root]
            stack = []

            while arr:
                node = arr.pop()
                if node.left:
                    arr.append(node.left)
                if node.right:
                    arr.append(node.right)

                stack.insert(0, node.data)

            return stack


if __name__ == "__main__":
    tree = Tree()
    nums = [1, 2, 3, 6, 7, 4, 5]
    [tree.insert(num) for num in nums]

    print(f"Tree in reverse: {tree.print_reverse(tree.root_node)}")
