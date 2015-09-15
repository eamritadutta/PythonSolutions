# Singly Linked List

class Node:

    # Constructor
    def __init__(self, val, next):
        self.val = val
        self.next = next

class List:

    # Constructor
    def __init__(self):
        self.head = None

    def addNode(self, val):

        # first Node
        if self.head == None:
            self.head = Node(val, None)

        else:
            self.head = Node(val, self.head)

    def printList(self):

        if self.head == None:
            print "Empty list passed - in for printing..."

        # print list recursively
        self.printListRecursively(self.head)


    def printListRecursively(self, start):

        # base case
        if start == None:
            return

        print str(start.val) + "->"
        self.printListRecursively(start.next)

    def deleteNode(self, val):

        # deletes node recursively
        if self.deleteNodeRecursively(self.head, None, val) == True:

            print "Node with value: " + str(val) + " has been deleted."

        else:

            print "Node with value: " + str(val) + " has not been found in the list. No node has been deleted."

    def deleteNodeRecursively(self, start, prev, val):

        # base case
        if start == None:
            return False

        # we are at the node to be deleted
        if start.val == val:

            # deleting head when there is only 1 node in the list
            if start.next == None and prev == None:
                self.head = None

            # deleting head in a list when # of nodes in list > 1
            elif start.next != None and prev == None:
                self.head = start.next

            # deleting a node when it is the last node
            elif start.next == None:
                prev.next = None

            # delete a node when next can be node
            else:
                prev.next = start.next

            return True

        # we are not at the node to be deleted
        else:
            return self.deleteNodeRecursively(start.next, start, val)



l = List()
l.addNode(1)
l.addNode(5)
l.addNode(9)
l.addNode(11)
l.printList()

l.deleteNode(9)
l.printList()

l.deleteNode(11)
l.printList()

l.deleteNode(5)
l.printList()

l.deleteNode(1)
l.printList()
