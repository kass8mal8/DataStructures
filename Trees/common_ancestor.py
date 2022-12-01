""" Give an algorithm for finding least common ancestor of two nodes """

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
            return
        else:
            node = Node(data)
            current = self.root_node
            parent = None

            while True:
                parent = current
                if current.data < node.data:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

                else:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return

    def preorder(self, root, arr):
        if root is None:
            return
        else:
            self.preorder(root.left_child, arr)
            arr.append(root.data)
            self.preorder(root.right_child, arr)

        return arr

    def lca(self, root, alpha, beta):
        if root is None:
            return
        if root.data == alpha or root.data == beta:
            return root.data
        else:
            left, right = self.lca(root.left_child, alpha, beta), self.lca(root.right_child, alpha, beta)

            if left and right: return root.data
            else: return left if left else right


if __name__ == "__main__":
    tree = Tree()
    nums = [20, 17, 15, 19, 23, 27]

    [tree.insert(num) for num in nums]
    print(tree.preorder(tree.root_node, []))
    print(f"Least Common Ancestor:{tree.lca(tree.root_node, 23, 17)}")
