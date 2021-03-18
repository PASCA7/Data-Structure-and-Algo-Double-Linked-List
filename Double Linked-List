# Create a Node

class Nodes:
    def __init__(self, data):
        self.back = None
        self.element = data
        self.next = None
        
        
# Assign a Head element None        

class Doublly:
    def __init__(self):
        self.head = None
        
        
# insert the element in empty Linked-List  
    
    def insert_into_empty(self, data):
        if self.head is None:
            new_node = Nodes(data)
            self.head = new_node
        else:
            print("list is not empty")
            
            
#insert The element/data at the starting of head Node       
            
    def insert_at_starts(self,data):
        if self.head is None:
            new_node = Nodes(data)
            self.head = new_node
            print("node insert")
            return
            
        new_node = Nodes(data)
        new_node.next = self.head
        self.head.back = new_node
        self.head = new_node  
        

#interate the element or visiting each Node
        
    def triverse(self):
        if self.head is None:
            print("list has no element")
            return
        n = self.head
        while n is not None:
            print(n.element)
            prev = n.back
            n = n.next
            
            
            
