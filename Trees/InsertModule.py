class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    node = Node(data)
    if root is None:
        root = node
        return
    else:
        current = root
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
