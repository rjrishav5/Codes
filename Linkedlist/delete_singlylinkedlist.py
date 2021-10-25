class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

#insering node at end  

    def insert_at_end(self,data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node

#deleting node from begining

    def from_begining(self):
        if (self.head == None):
            print("\nThe list is already empty")
        else:
            deletenode = self.head
            self.head = self.head.next
            deletenode = None
    
#deleting node from end
    def from_end(self):
        if(self.head.next == None):
            self.head = None
        else:
            temp = self.head
            while(temp.next.next != None):
                temp = temp.next
            deletenode = temp.next
            temp.next = None
            deletenode = None

#delete node from position 
# 
    def from_position(self,position):
        if(position<1):
            print("\n position should be >=1")
            return
        elif(position == 1 and self.head != None):
            deletenode = self.head
            self.head = self.head.next
            deletenode = None
        else:
            temp = self.head
            for i in range(1,position-1):
                if (temp != None):
                    temp = temp.next
            if (temp != None and temp.next != None):
                deletenode = temp.next
                temp.next = temp.next.next
                deletenode = None
            else:
                print("\n The node is already null")
#printing linkedlist

    def printlist(self):
        temp = self.head
        if (temp != None):
            print("\nThe list contains:")
            while(temp != None):
                print(temp.data,end=" ")
                temp = temp.next
        else:
            print("\n The list is empty")



llist = linkedlist()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(5)        
llist.printlist()
llist.from_begining()
llist.printlist()
llist.from_end()
llist.printlist()
llist.insert_at_end(80)
llist.insert_at_end(100)
llist.printlist()
llist.from_position(2)
llist.printlist()





