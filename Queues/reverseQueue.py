class Stack :
    def __init__(self) -> None:
        self.items = []
        
    def push (self,data):
        self.items.append(data)
        
    def pop (self):
        return self.items.pop()

class Queue :
    def __init__(self) -> None:
        self.reverse_items = []
        
    def Queue (self,data) :
        
        
    def pop (self):
        reverse_items = self.reverse_items.append(self.items.pop())
        return reverse_items