class Node:
    data = None
    next = None
    prev = None

    def __init__ (self, data):
        self.data = data

class DoubleLinklist:
    head = None

    def __init__ (self, data=None):
       self.head = None

    def printDoubleLinkList(self):
        if self.head is None: 
            print("Empty List")
            print("+++++++++")
            return
        current = self.head
        while current is not None:
           print(str(current.data) + "=>")
           current = current.next
        
        print("+++++++++")
         
    def append(self, data):
        newNode = Node(data)
        if self.head is None: 
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            newNode.prev = current
            current.next = newNode

    def prepend(self, data):
        newNode = Node(data)
        if self.head is None: 
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
    
    def remove(self, key):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            if current.data == key:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                return
            current = current.next

dll = DoubleLinklist()
dll.printDoubleLinkList()
dll.prepend(1)
dll.printDoubleLinkList()
dll.append(2)
dll.printDoubleLinkList()
dll.append(3)
dll.printDoubleLinkList()
dll.prepend(0)
dll.printDoubleLinkList()




