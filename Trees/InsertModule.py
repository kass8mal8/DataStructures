from Trees.BinaryTree import Node


def insert(root, data):
    node = Node(data)

    if root is None:
        root = node
    else:
        current = root
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
