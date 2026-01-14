"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the 
beginning of the loop. 
DEFINITION 
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so 
as to make a loop in the linked list. 
EXAMPLE 
Input: A->8->C->D->E- > C [the same C as earlier] 
Output: C

"""

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def hasCycle(head):

    if not head:
        return False
    if head and not head.next:
        return False
    
    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True

    return False

def getCycleStart(head):

    if not head:
        return "No Cycle"
    if head and not head.next:
        return "No Cycle"
    
    fast = head
    slow = head
    hasCycle = False
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            hasCycle = True
            break
    if hasCycle:
        slow = head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow.data
        
    return "No Cycle"


    

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    # Create a singly linked list:
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next



    ans = hasCycle(head)
    ans2 = getCycleStart(head)
    print(ans)
    print(ans2)

