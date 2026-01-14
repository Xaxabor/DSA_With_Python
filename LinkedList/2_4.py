"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come 
before all nodes greater than or equal to x. Ifxis contained within the list, the values of x only need 
to be after the elements less than x (see below). The partition element x can appear anywhere in the 
"right partition"; it does not need to appear between the left and right partitions. 
EXAMPLE 
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5] 
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def partition(head, x):
    if head is None:
        return head
    curr = head
    target = None
    while curr:
        if not target and curr.data >= x:
            target = curr
        elif target and curr.data < x:
            target.data, curr.data = curr.data, target.data
            target = target.next
            while target:
                if target.data >= x:
                    break
                target = target.next
            if not target:
                break
        curr = curr.next

    return head

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    # Create a singly linked list:
    # 2 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
    head = Node(2)
    head.next = Node(5)
    head.next.next = Node(8)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next = Node(1)

    head = partition(head, 5)
    print_list(head)

