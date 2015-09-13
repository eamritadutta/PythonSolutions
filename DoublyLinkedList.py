# Doubly Linked List with head and tail pointer

class ListNode:

    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class List:

    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, val):

        # first Node
        if self.head == None and self.tail == None:
            self.head = ListNode(val, None, None)
            self.tail = self.head

        # 2nd Node
        elif self.head != None and self.head == self.tail:
            # create a new node and make the tail pointer point to it now
            self.tail = ListNode(val, self.head, None)

            # change the head's next
            self.head.next = self.tail

        # any other node
        else:
            self.tail.next = ListNode(val, self.tail, None)
            self.tail = self.tail.next
            #print "tail: " + str(self.tail)

    def printList(self):
        self.printListRecursively(self.head)


    def printListRecursively(self, start):

        if start == None:
            print "List is empty. Nothing to print."

        while start != None:
            if start.next == None:
                print start.val
            else:
                print str(start.val) + "->"

            start = start.next

    def reverseList(self):
        self.reverseListRecursively(self.head)


    def reverseListRecursively(self, start):

        if start == None:
            print "Empty List. Returning..."
            return

        # the following check will stand good and not swap values if there is
        # only 1 node in the list
        while start != None:
            # when we reach the original end node, make that node the head
            if start.next == None:
                self.head = start

            # when we are at the original first node, change the tail to point to it
            if start.prev == None:
                self.tail = start

            t = start.prev
            start.prev = start.next
            start.next = t
            start = start.prev

dll = List()

dll.addNode(1)
dll.addNode(5)
dll.addNode(9)
dll.printList()

dll.reverseList()
dll.printList()
