# node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# linked list class
class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            temp = self.tail
            self.tail = Node(val)
            temp.next = self.tail

    def printList(self):
        temp = self.head

        while temp is not None:
            if temp.next is not None:
                print str(temp.val) + "->"
            else :
                print str(temp.val)

            temp = temp.next

def interleave(list1, list2):

    head = None

    if list1 and list1.head != None:
        print "head assigned to l1's head"
        head = list1.head
    elif list2 and list2.head != None:
        print "head assigned to l2's head"
        head = list2.head
    else:
        return

    l1 = list1.head
    l2 = list2.head

    while l1 != None and l2 != None:
        n1 = l1.next
        n2 = l2.next

        l1.next = l2
        if n1 != None:
            l2.next = n1

        l1 = n1
        l2 = n2

    # the following is strictly for debugging
    p_head = head
    while p_head != None:
        print str(p_head.val) + "->"
        p_head = p_head.next

    return head

# test the List class
l1 = List()
l1.add(1)
l1.add(4)
# l1.add(7)
# l1.add(87)
# l1.add(97)
# l1.add(107)
l1.printList()
print

l2 = List()
l2.add(3)
l2.add(14)
l2.add(47)
l2.add(57)
# l2.add(67)
# l2.add(77)
l2.printList()
print

interleave(l1, l2)
# interleave(None, None)
