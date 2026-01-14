"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def kth_from_end1(head, k):
    if head is None:
        return None
    c = 0
    temp =head
    while temp:
        c=c+1
        temp=temp.next

    if c < k:
        return "Wrong Input"
    
    temp = head

    for i in range(c-k):
        temp = temp.next
    return temp.data

def kth_from_end2(head, k):
    if head is None:
        return None
    fast = head
    slow = head

    while k>0:
        if fast is None:
            return "Wrong Input"
        fast = fast.next
        k-=1
    while fast:
        slow = slow.next
        fast = fast.next

    return slow.data

if __name__ == "__main__":
    # Create a singly linked list:
    # 12 -> 11 -> 12 -> 21 -> 41 -> 43 -> 21
    head = Node(12)
    head.next = Node(11)
    head.next.next = Node(12)
    head.next.next.next = Node(21)
    head.next.next.next.next = Node(41)
    head.next.next.next.next.next = Node(43)
    head.next.next.next.next.next.next = Node(21)

    kth_from_end_value = kth_from_end2(head, 3)
    print(kth_from_end_value)
