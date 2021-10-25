from insertSlinkedlist import Slinkedlist


def n_from_last(ll,n):
    point1 = ll.head
    point2 = ll.head
    for i in range(n):
        if point2 is None:
            return None
        point2 = point2.next
    while point2:
        point1 = point1.next
        point2 = point2.next
    return point1.data

customll = Slinkedlist()
customll.atEnd(10)
customll.atEnd(20)
customll.atEnd(30)
customll.atEnd(40)
customll.atEnd(50)
customll.atEnd(60)
customll.print_linkedlist()
print('\n')
print(n_from_last(customll,2))