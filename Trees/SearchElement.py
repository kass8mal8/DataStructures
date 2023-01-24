""" Give an algorithm for searching an element in binary tree. """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def insert_left(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
            return
        else:
            node, current = Node(data), self.root_node
            node.left_child = current.left_child
            current.left_child = node

    def insert_right(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
            return
        else:
            node, current = Node(data), self.root_node
            node.right_child = current.right_child
            current.right_child = node

    @staticmethod
    def search(root, data):
        if not root:
            return 0
        else:
            arr, node = [root], None
            while arr:
                node = arr.pop()
                if node.data == data:
                    return "Data Found"

                if node.left_child:
                    arr.append(node.left_child)

                if node.right_child:
                    arr.append(node.right_child)

    def postorder(self, root, arr):
        if not root:
            return
        else:
            self.postorder(root.left_child, arr)
            self.postorder(root.right_child, arr)
            arr.append(root.data)

        return arr


if __name__ == "__main__":
    tree = Tree()
    nums = [19, 32, 13, 15, 38, 92]

    [tree.insert_left(num) for num in nums[:3]]
    [tree.insert_right(num) for num in nums[3:]]

    print(f"Tree:{tree.postorder(tree.root_node, [])}")
    print(tree.search(tree.root_node, 22))
