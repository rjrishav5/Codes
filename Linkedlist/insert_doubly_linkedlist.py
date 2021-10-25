class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linkedlist:
    def __init__(self):
        self.head = None
# insert node at the end of a doubly linkedlist

    def at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
# insert node at the begining of a doubly linkedlist

    def at_begining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
# insert node at a given position in doubly linkedlist
    def at_position(self,position,data):
        new_node = Node(data)
        if (position == 1):
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            i = 2
            while(i <=position-1):
                if(temp.next is not None):
                    temp = temp.next
                    i+=1
            if (temp.next is not None):
                new_node.next = temp.next
                new_node.prev = temp
                temp.next = new_node
                if(new_node.next is not None):
                    new_node.next.prev = new_node

# print the doubly linkedlist
    def print_llist(self):
        temp = self.head
        if (temp is not None):
            print("\nThe list contains:",end=" ")
            while(temp is not None):
                print(temp.data,end=" ")
                temp = temp.next
        else:
            print("The list is empty")
            


dllist = doubly_linkedlist()
dllist.at_end(2)
dllist.at_end(3)
dllist.at_end(4)
dllist.at_end(5)
dllist.at_end(6)
dllist.at_end(7)

dllist.print_llist()
dllist.at_position(3,15)
dllist.print_llist()
dllist.at_position(1,20)
dllist.print_llist()

            




