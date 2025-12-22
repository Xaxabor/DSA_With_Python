q = list([None]*5)
front = -1
rear = -1

def queue(value):
    global front
    global rear
    
    if rear==len(q)-1:
        print("queue Overflow")

    elif front==-1 and rear==-1:
        front+=1
        rear+=1
        q[rear]=value
    else:
        rear+=1
        q[rear]=value

def deq():
    global front
    global rear
    if front==-1 and rear==-1:
        print("queue Underflow")

    elif front==rear:
        value = q[front]
        print("dequeue :" + str(value))
        q[front]=None
        front=-1
        rear=-1
        return value

    else:
        value = q[front]
        print("dequeue :" + str(value))
        val = q[front]
        q[front]=None
        front +=1
        return value

if __name__ == "__main__":
    print(q)

    deq() #queue underflow    
    queue(1)   #1
    print(q) #1  
    deq() #1
    print(q) #empty
    queue(1) #1
    queue(2) #1->2
    queue(3) #1->2->3
    queue(4) #1->2->3->4
    queue(5) #1->2->3->4->5
    print(q) #1->2->3->4->5
    queue(6) #queue overflow
    deq() #1
    deq() #2
    deq() #3
    deq() #4
    deq() #5
    print(q) #None->None->None->None->None
    queue(6)
    print(q) #6->None->None->None->None