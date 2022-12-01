"""Stack implementation using linked lists"""

class Node :
    def __init__(self,data = None) -> None:
        self.data = data
        self.next = None
        
class Stack :
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        
    def push (self,data) :
        node = Node (data) 
        current = self.head
        
        if self.head is None :
            self.head = node
            return 
        else :
            while current.next :
                current= current.next
            current.next = node
            self.size += 1
            
    def pop (self) :
        current = self.head 
        
        while current.next :
            current = current.next
            
        return current.data
    
    def iter (self) :
        current = self.head 
        while current :
            val = current.data
            current = current.next
            yield val
    
stack = Stack ()

[stack.push(x) for x in ['AlgoExpert','LeetCode','Hackerrank']]
print([plat for plat in stack.iter()])
print(stack.pop())