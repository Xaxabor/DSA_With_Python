"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def reverseList (head):
    
    if not head or not head.next:
        return head

    prev = None
    curr = head

    while curr:
        temp= curr.next
        curr.next = prev
        prev = curr
        curr=temp

    return prev

def isPalindrome(head):
    fast = head
    slow = head

    if not head or not head.next:
        return True

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    if fast:
        slow = slow.next
    
    secondHalf = reverseList(slow)
    firstHalf = head
    while secondHalf:
        if firstHalf.data != secondHalf.data:
            return False
        firstHalf = firstHalf.next
        secondHalf = secondHalf.next

    return True
    

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
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(1)


    ans = isPalindrome(head)
    print(ans)

