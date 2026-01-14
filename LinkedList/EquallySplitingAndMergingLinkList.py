"""
For example ,  suppose  you  had  a  linked  list  
a1 ->a2 ->. .  .->an ->b1->b2->. .  .->bn  and  you  wanted  to rearrange  it  into  
a1 ->b1 ->a2 ->b2 -> .  .  .  ->an ->bn .  
You  do  not  know  the  length  of the  linked  list  (but  you do  know  that  the  length  is  an  even  number) . 
"""


class Node:

    data  = None
    next  = None

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    head = None

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head =newNode
            return self.head
        temp = self.head
        while(temp.next):
            temp = temp.next

        temp.next = newNode
        return self.head

    def printList(self):
        temp = self.head
        if temp == None:
            print("List is empty")
            return
        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")         

    def delete(self, value):
        temp = self.head
        if temp.data == value:
            self.head=self.head.next
            return self.head
        
        while(temp.next):
            if temp.next.data == value:
                temp.next=temp.next.next
                return self.head
            temp = temp.next
        print("Value not found")

    def prepend(self, data):
        nedNode = Node(data)
        newnode.next = self.head
        self.head = newnode
        return self.head

    def breakList(self):
        slow = self.head
        fast = self.head
        c = 0
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            c = c+1
        
        odd = self.head
        even = slow


        while(even):
            temp_odd = odd.next
            temp_even = even.next
            odd.next = even
            if temp_even is None:
                even.next = None
            else:    
                even.next = temp_odd
            odd = temp_odd
            even = temp_even

    


    
if __name__ == "__main__":
    list1 = LinkedList()
    list2 = LinkedList()

    # Creating first linked list: 1 -> 3 -> 5 -> 7 -> 9 -> 2 -> 4 -> 6 -> 8 -> 10
    for i in [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]:
        list1.append(i)

    print("First Linked List:")
    list1.printList()
    print("Equally splited and Merged Linked List:")
    list1.breakList()
    list1.printList()