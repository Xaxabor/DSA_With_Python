"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single 
digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a 
function that adds the two numbers and returns the sum as a linked list. 
EXAMPLE 
Input: (7- > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. 
Output: 2 -> 1 -> 9. That is, 912.
"""


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def add_two_numbers_given_reverse(head, head2):
    curr1 = head
    curr2 = head2
    prev = None
    s=0
    add = None

    while curr2 and curr1:
        s = s+curr2.data+curr1.data  
        curr1.data = s%10
        s = s//10
        prev = curr1
        curr1 = curr1.next
        curr2 = curr2.next

    while curr1:
        s = s+curr1.data  
        curr1.data = s%10
        s = s//10
        prev = curr1
        curr1 = curr1.next

    while curr2:
        s = s+curr2.data  
        prev.next = Node(s%10)
        s = s//10
        prev = prev.next
        curr2 = curr2.next

    if s>0:
        prev.next = Node(s)

    return head

def add_two_numbers_given(head, head2):
    

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    # Create a singly linked list:
    head2 = Node(9)
    head2.next = Node(9)
    head2.next.next = Node(9)

    head = Node(5)



    head = add_two_numbers_given_reverse(head, head2)
    print_list(head)

