class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class LinkList:
    head = None

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            newNode.next = None
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode
            newNode.next = None

    def prepend(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = None
        else:
            newNode.next = self.head
            self.head = newNode
    
    def addAfterKey(self, key, data):
        if self.head is None:
            print("Emprty head")
            return
        newNode = Node(data)
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == key :
                break
            else:
                currentNode = currentNode.next
        if currentNode is None:
            print("No such Key ")
            return
        elif currentNode.data == key and currentNode.next is None:
            currentNode.next = newNode
            newNode.next = None
        elif currentNode.data == key and currentNode.next is not None:
            temp = currentNode.next
            currentNode.next = newNode
            newNode.next = temp

    def remove(self, key):
        if self.head is None:
            print("Emprty head")
            return
        elif (self.head.data == key) and (self.head.next is None):
            self.head = None
        elif (self.head.data == key) and (self.head.next is not None):
            self.head = self.head.next
        else:
            currentNode = self.head
            while currentNode.next is not None:
                if currentNode.next.data == key :
                    break
                else:
                    currentNode = currentNode.next
            if currentNode.next is None:
                print("No such data ")
                return
            elif currentNode.next.data == key and currentNode.next.next is None:
                currentNode.next = None
            elif currentNode.next.data == key and currentNode.next.next is not None:
                currentNode.next= currentNode.next.next


    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(str(currentNode.data) + " ->")
            currentNode = currentNode.next
        print("=======")


if __name__ == "__main__":
    ll = LinkList()

    ll.append(5)
    ll.append(2)
    ll.append(3)
    ll.prepend(1)
    ll.addAfterKey(5, 4)
    ll.printList()
    ll.addAfterKey(3, 6)
    ll.printList()
    ll.remove(5)
    ll.printList()
    ll.remove(3)
    ll.printList()
    ll.remove(1)
    ll.printList()
    ll.remove(1)
    ll.printList()
    ll.remove(2)
    ll.printList()
    ll.remove(2)
    ll.printList()
    ll.addAfterKey(2, 7)
    ll.printList()
    ll.prepend(0)
    ll.printList()
