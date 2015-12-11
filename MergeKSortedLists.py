import sys
# merge K sorted lists where the lists are as follows:
# 3 4 10 12
# 1 5
# 7 11

def mergeKSortedLists(heads):
    pMinNode = None
    newHead = None

    # scan values at pHeads of each list
    while True:
        minV = sys.maxint
        minNode = None

        for h in heads: # n3, n1, n7

            if h is not None:
                if h.val < minV:
                    minV = h.val
                    minNode = h

        if minNode == None: # all lists have reached end
            break

        # for the selected minNode
        if pMinNode is None:
            pMinNode = minNode
            newHead = minNode
        else:
            pMinNode.next = minNode
            pMinNode = minNode

        heads.remove(minNode)
        heads.append(minNode.next)
    # once you come out of the while loop
    return newHead

class Node:
    def __init__(self, n, v):
        self.next = n
        self.val = v

def test():

    n12 = Node(None, 12)
    n10 = Node(n12, 10)
    n4 = Node(n10, 4)
    n3 = Node(n4, 3)

    n5 = Node(None, 5)
    n1 = Node(n5, 1)

    n11 = Node(None, 11)
    n7 = Node(n11, 7)

    newHead = mergeKSortedLists([n3, n1, n7])
    printList(newHead)

def printList(head):
    vals = []
    while head is not None:
        vals.append(head.val)
        head = head.next

    print " ".join(str(v) for v in vals)

# call test code
test()
