class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Slinkedlist:
    def __init__(self):
        self.head = None

#inserting a node at begining
    def atBegin(self,data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head  = new_node


#inserting a node at the end 

    def atEnd(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return 
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node

#insert a node at given position(ALL)
    def atposition(self,data,position):
        new_node = Node(data)
        if (position <1):
            print("\n position should be >=1")
        elif (position == 1):
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(1,position-1):
                if (temp !=None):
                    temp = temp.next
            if (temp != None):
                new_node.next = temp.next
                temp.next = new_node
            else:
                print("\nThe previous node is null")


#display the content of linkedlist

    def print_linkedlist(self):
        temp = self.head
        if (temp != None):
            print("The Linkedlist contains: ")
            while(temp != None):
                print(temp.data,end=" ")
                temp = temp.next
        else:
            print("The list is empty")

    def reverse_linkedlist(self):
        if self.head is None:
            return None
        else:
            arr = []
            while self.head:
                arr.append(self.head.data)
                self.head = self.head.next
            while arr:
                print(arr.pop(),end=' ')


llist = Slinkedlist()
llist.atEnd(10)
llist.atEnd(20)
llist.atEnd(30)
llist.atBegin(5)

llist.print_linkedlist()
print("\n")
llist.reverse_linkedlist()