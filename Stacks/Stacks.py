class Node:
    def __init__(self,data = None) -> None:
        self.next = None
        self.data = data
        
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0
        
    def append (self,data):
        node = Node (data)
        if self.top is None:
            self.top = node
            return 
        else:
            current = self.top
            while current.next:
                current = current.next
                
            current.next = node
            self.size += 1
            
    def pop (self):
        if self.top is None:
            return 
        else:
            current = self.top
            previous = self.top
            while current.next:
                previous = current
                current = current.next
              
            previous.next = None
            self.size -= 1
            return current.data
        
        
    def iter (self):
        current = self.top
        while current:
            val = current.data
            current = current.next
            yield val
            
        
stack = Stack()
nums = [21,34,29,15,20,37]

[stack.append(num) for num in nums]

print([num for num in stack.iter()])
print(stack.pop()) 



for x in range(stack.size):
    print(f"List:{[num for num in stack.iter()]}")
    print(f"Last element:{stack.pop()}") 