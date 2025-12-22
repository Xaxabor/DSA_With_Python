stack = list([None]*5)
top = -1

def push(value):
    global top
    if top==len(stack)-1:
        print("Stack Overflow")
    else:
        top+=1
        stack[top]=value

def pop():
    global top
    if top==-1:
        print("Stack Underflow")
    else:
        print(stack[top])
        val = stack[top]
        stack[top]=None
        top -=1
        return val

if __name__ == "__main__":

    print(stack)

    pop() #stack underflow    
    push(1)   #1
    print(stack) #1  
    pop() #1
    print(stack) #empty
    push(1) #1
    push(2) #1->2
    push(3) #1->2->3
    push(4) #1->2->3->4
    push(5) #1->2->3->4->5
    print(stack) #1->2->3->4->5
    push(6) #stack overflow
    pop() #5
    pop() #5
    pop() #5
    pop() #5
    pop() #5
    print(stack) #1->2->3->4->None
    push(6)
    print(stack) #1->2->3->4->6