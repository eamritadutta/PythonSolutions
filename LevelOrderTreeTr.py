import Queue
class Node:
    def __init__(self, l, r, v):
        self.left = l
        self.right = r
        self.val = v

def levelT(root):
    if not root:
        return

    nodesInClevel = 1
    nodesInNlevel = 0

    q = Queue.Queue()
    q.put(root)

    while not q.empty():

        node = q.get()
        print node.val

        if node.left:
            q.put(node.left)
            nodesInNlevel += 1

        if node.right:
            q.put(node.right)
            nodesInNlevel += 1

        nodesInClevel -= 1
        # check and print blank line
        if nodesInClevel == 0:
            print
            nodesInClevel = nodesInNlevel
            nodesInNlevel = 0

        if nodesInClevel == 0:
            break

def test():
    # create the tree bottom up
    node4 = Node(None, None, 4)
    node5 = Node(None, None, 5)
    node6 = Node(None, None, 6)
    node7 = Node(None, None, 7)

    node2 = Node(node4, node5, 2)
    node3 = Node(node6, node7, 3)

    node1 = Node(node2, node3, 1)

    levelT(node1)

test()
