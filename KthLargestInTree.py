# delete a node in a Binary Search Tree

class TreeNode:

    # constructor
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Tree:

    # constructor
    def __init__(self):
        self.root = None

    def add(self, node, val): # node = 15, val = 10

        #print "Called add with val: " + str(val)

        # base case for stopping recursion
        if node == None:
            # print "Creating new Tree Node with value: " + str(val)
            newNode = TreeNode(val, None, None)

            if self.root == None:
                print "Root has been assigned as: " + str(newNode.val)
                self.root = newNode

            return newNode


        if val <= node.val:
            # print "adding " + str(val)
            #print "val <= node.val " + str(val) + str(node.val)

            x = self.add(node.left, val)
            if node.left == None:
                node.left = x


        if val > node.val:
            # print "adding " + str(val)
            #print "val > node.val " + str(val) + str(node.val)
            y = self.add(node.right, val)
            if node.right == None:
                node.right = y


    # add 1 new node with value 'val' to the tree
    def addNode(self, val):
        # the call to the following function will recursively check where to # add the new val, and when it finds the location, will create and
        # add a new node to the tree with root as 'root'

        if self.root is not None:
            print "Root is: " + str(self.root.val)  + ". Making call to add: " + str(val)

            if self.root.left is not None:
                print "root's left" + str(self.root.left.val)

            if self.root.right is not None:
                print "root's right" +  str(self.root.right.val)


        self.add(self.root, val)

    def findKthLargestNode(self, k):

        c = self.findKthLargestNodeRecursively(self.root, k, 0)

        if k > c or k <= 0:
            print "Node with rank: " + str(k) + " could not be found in tree."


    def findKthLargestNodeRecursively(self, start, k, c):

        # only if root is absent meaning that the tree does not have nodes
        if start == None:
            return c

        # base case - any leaf node with 0 children
        if start.left == None and start.right == None:
            c += 1
            if c == k:
                print "Kth largest node(where k is: " + str(k) + ") has the value: " + str(start.val)
            return c

        # get the # of nodes on the left
        c = self.findKthLargestNodeRecursively(start.left, k, c)

        # increment count to account for the current node
        c += 1

        if c == k:
            print "Kth largest node(where k is: " + str(k) + ") has the value: " + str(start.val)
            return c

        # get the # of nodes on the left
        c = self.findKthLargestNodeRecursively(start.right, k, c)
        return c


    def printTree(self):

        # prints a tree recursively using depth first traversal
        self.printT(self.root)

    def printT(self, start):

        if start == None:
            return

        print start.val

        self.printT(start.left)
        self.printT(start.right)


t = Tree()

t.addNode(15)
t.addNode(10)
t.addNode(5)
t.addNode(100)
t.addNode(1)
t.addNode(200)

print "------- Printing Original Tree --------"
t.printTree()

t.findKthLargestNode(1)

t.findKthLargestNode(2)

t.findKthLargestNode(3)

t.findKthLargestNode(4)

t.findKthLargestNode(5)

t.findKthLargestNode(6)

t.findKthLargestNode(10)

t.findKthLargestNode(0)
t.findKthLargestNode(-1)
