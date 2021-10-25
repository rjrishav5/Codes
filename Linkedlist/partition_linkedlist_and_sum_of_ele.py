


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class llist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        return self.tail


def part(ll,x):
    current = ll.head
    ll.tail = ll.head
    while current:
        next_node = current.next
        current.next = None
        if current.data < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node
    if ll.tail.next is not None:
        ll.tail.next = None
def print_ll(ll):
    temp = ll.head
    if (temp != None):
        print("The Linkedlist contains: ")
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next
        #print()
    else:
        print("The list is empty")  

def sum_of_ll(ll):
    total = 0
    temp = ll.head
    while temp is not None:
        total += temp.data
        temp = temp.next
    return total



customll = llist()
customll.add(10)
customll.add(100)
customll.add(30)
customll.add(80)
customll.add(20)
customll.add(15)
print_ll(customll)
part(customll,50)
print('\n')
print('The sum of elements in the linkedlist:',sum_of_ll(customll))
print_ll(customll)
