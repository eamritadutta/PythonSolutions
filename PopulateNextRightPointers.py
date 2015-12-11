# populate next right pointers
#        1
#    2       3
# 4    5   7   8
def populate(root):
    if not root:
        return

    curr = root # 1
    headNextLevel = None # None
    pNodeInNextLevel = None # None

    while curr: # 1

        while curr: # for all nodes in 1 level

            if curr.left:
                if pNodeInNextLevel:
                    pNodeInNextLevel.next = curr.left
                else:
                    headNextLevel = curr.left
                pNodeInNextLevel = curr.left

            if curr.right: # 1.3
                if pNodeInNextLevel: # 2
                    pNodeInNextLevel.next = curr.right
                else:
                    headNextLevel = curr.right
                pNodeInNextLevel = curr.right

            # change the curr node to the next node in the same level.
            # this is possible since the level we are currently in, is threaded
            curr = curr.next

        # once we are done with all the nodes in the curr level,
        # move to the head of the next level
        curr = headNextLevel
        headNextLevel = None # None
        pNodeInNextLevel = None # None

class TNode:
    def __init__(self, v, l, r, n):
        self.val = v
        self.left = l
        self.right = r
        self.next = n

def printLevelOrder(root):
    if not root:
        return

    curr = root
    headNextLevel = None
    while curr: # 1

        vals_in_level = []
        while curr: # for all nodes in 1 level
            vals_in_level.append(curr.val)

            if curr.left:
                if not headNextLevel:
                    headNextLevel = curr.left

            if curr.right: # 1.3
                if not headNextLevel:
                    headNextLevel = curr.right

            # change the curr node to the next node in the same level.
            # this is possible since the level we are currently in, is threaded
            curr = curr.next

        # once we are done with all the nodes in the curr level,
        # move to the head of the next level
        curr = headNextLevel
        headNextLevel = None # None
        print vals_in_level
        vals_in_level = []

# the test code
def test():

    # create tree bottom up
    #        1
    #    2       3
    # 4    5   7   8
    n4 = TNode(4, None, None, None)
    n5 = TNode(5, None, None, None)

    n2 = TNode(2, n4, n5, None)

    n7 = TNode(7, None, None, None)
    n8 = TNode(8, None, None, None)

    n3 = TNode(3, n7, n8, None)

    root = TNode(1, n2, n3, None)

    populate(root)

    printLevelOrder(root)

# call test code
test()
