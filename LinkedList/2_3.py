"""
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to 
that node. 
EXAMPLE 
Input: the node c from the linked list a - >b- >c - >d - >e- >f 
Result: nothing is returned, but the new linked list looks like a->b->d->e-> f
"""


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def delete_pointed_node(head, val):
    curr = head
    while curr:
        if curr.data == val:
            break
        curr = curr.next
    
    if curr is None:
        print("Value not found in the list.")
        return head

    curr.data = curr.next.data
    curr.next=curr.next.next
    return head
    


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    # Create a singly linked list:
    # 12 -> 11 -> 10 -> 21 -> 41 -> 43 -> 22
    head = Node(12)
    head.next = Node(11)
    head.next.next = Node(10)
    head.next.next.next = Node(21)
    head.next.next.next.next = Node(41)
    head.next.next.next.next.next = Node(43)
    head.next.next.next.next.next.next = Node(22)

    head = delete_pointed_node(head, 414)
    print_list(head)

