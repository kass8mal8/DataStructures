class Node :
    def __init__(self,data = None) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None
        
class Tree:
    def __init__(self) -> None:
        self.root_node = None
    
    def append (self,data):
        node = Node (data)
        
        if self.root_node is None:
            self.root_node = node
            return
        else :
            current = self.root_node
            parent = None
            
            while True:
                parent = current
                
                if current.data < node.data :
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return 
                    
                else :
                    current = current.left_child 
                    if current is None:
                        parent.left_child = node
                        return 
    
    
    def find_deepest (self,root_node):
        if root_node is None:
            return 
        else :
            queue = []
            queue.append(root_node)
            node = None
            
            while queue:
                node = queue.pop()
                if node.left_child is not None:
                    queue.append(node.left_child)
                if node.right_child is not None :
                    queue.append(node.right_child)
                    
            return node.data
    
    def preorder_traversal (self,root_node,array):
        if root_node is None:
            return 
        else :
            array.append(root_node.data)
            self.preorder_traversal(root_node.left_child,array)
            self.preorder_traversal(root_node.right_child,array)
            
        return array
    
    def print_tree (self):
        print(self.preorder_traversal(tree.root_node,[]))
        print(f"Deepest node:{self.find_deepest(tree.root_node)}")
        
        
tree = Tree ()
[tree.append(x) for x in ['Lisa','Elsie','Jael','Aisha','Alice']]
tree.print_tree()                    