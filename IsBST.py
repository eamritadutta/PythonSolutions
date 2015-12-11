import sys

def isBst(n):
    if not n:
        return False

    minv = -sys.maxint
    maxv = sys.maxint

    return isBstRec(n, minv, maxv)

def isBstRec(n, minv, maxv):

    print "n: " + str(n.val) + " minv: " + str(minv) + " maxv: " + str(maxv)

    if n == None:
        return True

    # no left and right
    if n.left == None and n.right == None:
        return (n.val > minv and n.val < maxv)

    if n.val > minv and n.val < maxv:
        return (isBstRec(n.left, minv, n.val) and isBstRec(n.right, n.val, maxv))

    else:
        return False

class Node():
    def __init__(self, l, r, v):
        self.left = l
        self.right = r
        self.val = v

def test():

    n3 = Node(None, None, 3)
    n1 = Node(None, None, 1)
    n2 = Node(n1, n3, 2)

    print isBst(n2)

test()
