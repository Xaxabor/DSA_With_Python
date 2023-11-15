class Node:
    data = None
    next = None 
    
    def __init__ (self, data):
        self.data = data
        self.next = None
        
        
class LinkList:
    
    nCount = 0
    root = None
    
    def __init__(self):
        nCount = 0
    
    def append(self, data):
        
        newData = Node(data)
        
        if self.root == None:
            self.root  = newData
            self.nCount +=1
            
        else:
            temp = self.root
            while(temp.next is not None):
                temp = temp.next
                
            temp.next = newData
            self.nCount +=1
    
    def prepend(self, data):
        
        newData = Node(data)
        
        if self.root == None:
            self.root  = newData
            self.nCount = self.nCount  + 1 
            
        else:
            newData.next = self.root
            self.root = newData
            self.nCount +=1

    
    def pop(self):
        temp = self.root
        if temp is None:
            print("No node left");
            
        elif temp.next is None:
            self.root = None
            self.nCount -=1
        
        else:
            while(temp.next.next is not None):
                temp = temp.next
                self.nCount -=1
        
            temp.next = None

    def removeRoot(self):
        if self.root is None:
            print("No node left");
            
        elif self.root.next is None:
            self.root = None
            self.nCount -=1
        
        else:
            temp = self.root.next
            self.root = temp
            self.nCount -=1
          
            
    def show(self):
        
        temp = self.root
        
        if temp is None:
            print("No node left");
        
        else:
            print("Current Node count : " + str(self.nCount));
            while(temp.next is not None):
                print(temp.data)
                temp = temp.next
        
            print(temp.data);
        print("=============")

    # def currentNodeCount(self):
    #     count = 0
    #     if self.root is None:
    #         return count          
    #     else:
    #         temp = self.root
    #         while(temp is not None):
    #             count +=1
    #             temp = temp.next

    #         self.nCount = count

    #         return count
            
            
if __name__ == "__main__":
    
    ll = LinkList()

    ll.removeRoot()
    ll.show()
    
    ll.prepend(1)
    ll.show()

    ll.removeRoot()
    ll.show()

    ll.append(5)
    ll.append(3)
    ll.append(2)
    ll.prepend(0)
    ll.show()
    
    ll.removeRoot()
    ll.show()

    # ll.pop()
    # ll.show()

    # ll.pop()
    # ll.show()

    ll.removeRoot()
    ll.show()


        
        
        
            