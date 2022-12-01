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

    def preorder_traversal(self, root_node, arr):
        if root_node is None:
            return
        else:
            arr.append(root_node.data)
            self.preorder_traversal(root_node.left_child, arr)
            self.preorder_traversal(root_node.right_child, arr)

        return arr

    def print_tree(self):
        print(f'Tree values: {self.preorder_traversal(tree.root_node, [])}')

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current.data

    def delete(self, data):
        if data < self.data:
            if self.left_child:
                self.left_child.delete(data)
        elif data > self.data:
            if self.right_child:
                self.right_child.delete(data)
        else:
            if self.left_child is None and self.right_child is None:
                return None
            if self.left_child:
                return self.right_child
            if self.right_child:
                return self.left_child


tree = Tree()
nums = [12, 10, 26, 18, 43]
[tree.insert(num) for num in nums]
print(f"Minimum: {tree.find_min()}")
tree.print_tree()
