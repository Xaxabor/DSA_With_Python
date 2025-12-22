class Node:
    data = None
    next = None

    def __init__ (self, data):
        self.data=data
        self.next = None

class Queue:
    front = None
    rear = None
    nCount = 0
    size = 0
    
    def __init__(self, size):
        self.size=size
        self.nCount=0
        self.front=None
        self.rear=None


    def enqueue(self, data):
        newNode = Node(data)
        if self.rear is None and self.front is None:
            self.rear=newNode
            self.front=newNode
            self.nCount +=1
        elif self.nCount == self.size:
            print("Queue Overflow")
        else:
            self.rear.next = newNode
            self.rear = newNode
            self.nCount +=1
    
    def dequeue(self):
        if self.front is None and self.rear is None:
            print("Queue Underflow")
        elif self.front == self.rear:
            print("Dequeued value: " + str(self.front.data))
            self.rear = None
            self.front = None
            self.nCount -=1
        else:
            print("Dequeued value: " + str(self.front.data))
            self.front = self.front.next
            self.nCount -=1

    def display(self):
        temp = self.front
        if temp is None:
            print("No node to print")
            return
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    q = Queue(5)

    q.dequeue() #queue underflow
    q.enqueue(1) #1
    q.display() #1
    q.dequeue() #1
    q.display() #empty
    q.enqueue(1) #1
    q.enqueue(2) #1->2
    q.enqueue(3) #1->2->3
    q.enqueue(4) #1->2->3->4
    q.enqueue(5) #1->2->3->4->5
    q.display() #1->2->3->4->5
    q.enqueue(6) #queue overflow
    q.dequeue() #1
    q.dequeue() #2
    q.dequeue() #3
    q.dequeue() #4
    q.dequeue() #5
    q.display() #empty
    q.enqueue(6)
    q.display() #6
        