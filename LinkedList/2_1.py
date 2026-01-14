# Python program to remove duplicates from an 
# unsorted linked list

"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.

FOLLOW UP 
How would you solve this problem if a temporary buffer is not allowed? 
ans at bottom of file
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def remove_duplicates(head):
    if head is None or head.next is None:
        return head
    
    seen=set()

    temp=head
    prev=None

    while temp:
        if temp.data in seen:
            prev.next=temp.next
        else:
            seen.add(temp.data)
            prev=temp
        temp=temp.next

    return head


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

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

    head = remove_duplicates(head)
    print_list(head)



















    #then we can use two pointers, one pointer will iterate through the linked list while the other pointer will check for duplicates for the current node pointed by the first pointer.