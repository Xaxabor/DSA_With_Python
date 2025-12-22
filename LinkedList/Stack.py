class Node:
    data = None
    next = None 
    
    def __init__ (self, data):
        self.data = data
        self.next = None
        
        
class Stack:
    
    nCount = 0
    top = None
    size = 0
    
    def __init__(self, size):
        self.nCount = 0
        self.size = size
        self.top = None
    
    def push(self, data):
        newData = Node(data)
        if self.top == None:
            self.top  = newData
            self.nCount +=1
        elif self.nCount == self.size:
            print("Stack Overflow")
        else:
            newData.next = self.top
            self.top = newData
            self.nCount +=1
    
    def pop(self):
        if self.top==None:
            print("stack underflow")
        else:
            temp = self.top
            self.top = self.top.next
            self.nCount -=1
            print("Popped value: " + str(temp.data))
            return temp.data

    def peak(self):
        if self.top is None:
            print("No node left")
        else:
            print("Top value: " + str(self.top.data))
            return self.top.data
          
            
    def display(self):
        temp = self.top
        
        if temp is None:
            print("No node to print")
        
        else:
            print("Current Node count : " + str(self.nCount));
            while(temp is not None):
                print(temp.data)
                temp = temp.next
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
    
    s = Stack(5)

    s.pop() #stack underflow    
    s.push(1)   #1
    s.display() #1    
    s.pop() #1
    s.display() #empty

    s.push(5) #5
    s.push(4) #4->5
    s.push(3) #3->4->5
    s.display()
    s.peak() #3
    s.push(2) #2->3->4->5
    s.push(1) #1->2->3->4->5
    s.display() #1->2->3->4->5
    s.push(0) #stack overflow
    s.push(0) #stack overflow
    s.pop() #1
    s.display() #2->3->4->5
    s.peak() #2


        
        
        
            