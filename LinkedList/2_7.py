"""
Intersection; Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. 
Note that the intersection is defined based on reference, not value. That is, if the kth 
node of the first linked list is the exact same node (by reference) as the jt h node of the second 
linked list, then they are intersecting. 
"""


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def getIntersectionNode(headA, headB):
    ca =0
    cb =0
    temp = headA
    while temp:
        temp=temp.next
        ca +=1
    
    temp = headB
    while temp:
        temp=temp.next
        cb +=1

    tempA = headA
    tempB = headB
    
    if ca>cb:
        d =ca-cb
        while d>0:
            tempA = tempA.next
            d -=1

    elif cb>ca:
        d =cb-ca
        while d>0:
            tempB = tempB.next
            d -=1

    while tempA and tempB:
        if tempA.data == tempB.data:
            return tempA.data
        tempA = tempA.next
        tempB = tempB.next

    return None


if __name__ == "__main__":
    # Create a singly linked list:
    #[4,2,8,4,5]
    head = Node(4)
    head.next = Node(2)
    head.next.next = Node(8)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    #[5,6,1,8,4,5]
    head2 = Node(5)
    head2.next = Node(6)
    head2.next.next = Node(1)
    head2.next.next.next = Node(8)
    head2.next.next.next.next = Node(4)
    head2.next.next.next.next.next = Node(5)


    ans = getIntersectionNode(head, head2)
    print(ans)

