class Node:
    data = None
    next = None

    def __init__ (self, data):
        self.data = data
        self.next = None


class LinkList:
    root = None

    def __init__(self):
        self.root = None


    def append(self, data):
        newNode = Node(data)

        if self.root == None:
            self.root = newNode

        else:
            temp = self.root
            while(temp.next is not None):
                temp = temp.next
            temp.next= newNode

    def prepend(self, data):
        newNode = Node(data)

        if self.root == None:
            self.root = newNode

        else:
            newNode.next = self.root
            self.root = newNode

    def show(self):
        if(self.root == None):
            print("Empty!!!")
        temp = self.root
        while(temp is not None):
            print(temp.data)
            temp = temp.next
        
        print("--------------")

    def reverse(self):
        if(self.root == None):
            print("Can not reverse Empty list!!!")

        elif(self.root.next == None):
            pass

        else:
            temp = self.root
            temp2 = self.root.next
            temp.next = None
            while(temp2 is not None):
                temp3 = temp2.next
                temp2.next = temp
                temp = temp2
                temp2 = temp3
            
            self.root = temp



if __name__ == "__main__":

    ll = LinkList()

    ll.append(1)
    ll.append(2)
    # ll.append(3)
    ll.prepend(0)
    # ll.append(4)
    # ll.append(5)
    # ll.append(6)
    ll.show()

    ll.reverse()
    ll.show()

