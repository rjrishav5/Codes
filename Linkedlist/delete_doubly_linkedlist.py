class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linkedlist:
    def __init__(self):
        self.head = None
    

    def at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while (temp.next is not None):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def from_begining(self):
        if self.head is None:
            print("\nThe list is empty ")
        else:
            deletenode = self.head
            self.head = self.head.next
            deletenode = None
            self.head.prev = None

    def from_end(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while(temp.next.next is not None):
                    temp = temp.next
                lastnode = temp.next
                lastnode = None
                temp.next = None
    
    def from_position(self,position):
        if position == 1 and self.head is not None:
            deletenode = self.head
            self.head = self.head.next
            deletenode = None
            self.head.prev = None
        else:
            temp = self.head
            i = 2
            while(i <= position-1):
                if temp is not None:
                    temp = temp.next
                i+=1
            if temp is not None and temp.next is not None:
                deletenode = temp.next
                temp.next = temp.next.next
                if temp.next.next is not None:
                    temp.next.next.prev = temp.next
                deletenode = None
            else:
                print("The node is already null")

    def print_list(self):
        if self.head is not None:
            print("\nThe list contains:",end=" ")
            temp = self.head
            while(temp is not None):
                print(temp.data,end=" ")
                temp = temp.next
        else:
            print("\nThe list is empty")

dllist = doubly_linkedlist()
dllist.at_end(1)
dllist.at_end(2)
dllist.at_end(3)
dllist.at_end(4)
dllist.at_end(5)
dllist.at_end(6)
dllist.print_list()
dllist.from_end()
dllist.print_list()
dllist.from_position(3)
dllist.print_list()
