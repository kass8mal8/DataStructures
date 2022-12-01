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

    @staticmethod
    def half_nodes(root):
        if root is None:
            return
        else:
            count, arr, node = 0, [root], None

            while arr:
                node = arr.pop()
                if (node.left_child and not node.right_child) or (node.right_child and not node.left_child):
                    count += 1
                else:
                    if node.left_child:
                        arr.append(node.left_child)
                    if node.right_child:
                        arr.append(node.right_child)
            return count

    def inorder_traversal(self, root, arr):
        if root is None:
            return
        else:
            arr.append(root.data)
            self.inorder_traversal(root.left_child, arr)
            self.inorder_traversal(root.right_child, arr)

        return arr


if __name__ == "__main__":
    tree = Tree()
    nums = [11, 7, 13, 5, 9, 12, 15, 6, 10, 17]
    [tree.insert(num) for num in nums]

    print(tree.inorder_traversal(tree.root_node, []))
    print(f"Half Nodes: {tree.half_nodes(tree.root_node)}")
