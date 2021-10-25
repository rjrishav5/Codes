from insertSlinkedlist import Slinkedlist


def del_dupli(ll):
    if ll.head is None:
        return 
    else:
        temp = ll.head
        visited = []
        while temp.next:
            if temp.next.data in visited:
                temp.next = temp.next.next
            else:
                visited.append(temp.next.data)
                temp = temp.next
        return ll


customll = Slinkedlist()
customll.atEnd(10)
customll.atEnd(20)
customll.atEnd(30)
customll.atEnd(40)
customll.atEnd(20)
customll.atEnd(60)
customll.print_linkedlist()
del_dupli(customll)
print("\n")
customll.print_linkedlist()