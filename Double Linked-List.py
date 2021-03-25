class node:
    def __init__(self,data, next=None, prev=None):
        self.prev = prev
        self.data = data
        self.next = next
        
class double:
    def __init__(self):
        self.head = None
    
    def empty(self,data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
            
            
    #insert at staring if list       
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
               
            
    #push the element after given data
    def after_element(self,x, ndata):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            pre = n
            n=n.next     
        if n is None:
            print("element is not found")
        else:
            new_node = node(ndata)
            new_node.next = self.head.next
            self.head.next = new_node
            new_node.prev = self.head
            
            
  
    #push the element before given data
    def before_element(self, x , data):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            pre = n
            n=n.next   
        if n is None:
            print("element is not found")
        else:
            new_node = node(data)
            new_node.next = pre.next
            pre.next = new_node
            new_node.prev = pre
        
        
        
     #visiting each element       
    def transv(self):
        if self.head is None:
            print("List has no Element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next
                
    
    #delete only middle element
    def delete(self,x):
        n = self.head
        if self.head is None:
            print("List has no Element")
            return
        else:
            while n is not None:
                if n.data == x:
                    print("element found !!!!")
                    break
                pre = n    
                n = n.next  
            if n == None:
                return
            pre.next = n.next
            
            
    #count the no of element      
    def count(self):
        c = 0
        if self.head is None:
            print("List has no Element")
            return
        else:
            n = self.head
            while n is not None:
                c += 1 
                n = n.next
                print(c)
        
    
        
