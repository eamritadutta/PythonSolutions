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

    # the following method will find the root with val and then delete it from
    # the tree and adjust the tree accordingly. for adjusting the tree accordingly, this function needs to keep track of the parent nodes as it
    # traverses the tree
    def deleteNode(self, val):

        # if the root is None, always do this sanity test
        if self.root == None:
            print "Empty tree passed-in to the deleteNode method. Returning."
            return

        # recursivly delete
        # pass - in the node where we start looking for val
        # also pass - in the value of the parent with each recursive call
        if self.deleteNodeRecursively(self.root, None, val) == False:
            print "Did not find node wiht value: " + str(val) + " in the given Tree. No node has been deleted."

        else:
            print "Deleted node with value: " + str(val) + " from the given Tree."

    def deleteNodeRecursively(self, start, parent, val):

        # base case - check if start is None, return false
        if start == None:
            return False

        # found the node to be deleted on the right of the parent
        if val == start.val and val > parent.val:
            # make the left child, if any of this node the right child of the parent. if not, make the right child of this node the right child of the parent
            if start.left != None:
                parent.right = start.left
            else:
                parent.right = start.right

        # found the node with 'val' to be deleted on the left of the parent node
        elif val == start.val and val <= parent.val:

            # check for left child of node with 'val'
            if start.left != None:
                parent.left = start.left
            else:
                parent.left = start.left

        # we did not find the node with 'val' to be deleted
        # have to check both the left and the right child of 'start'
        elif self.deleteNodeRecursively(start.left, start, val) == False:
                return self.deleteNodeRecursively(start.right, start, val)
        else:
            return False

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

t.deleteNode(100)
print "------- Printing Tree after deleting node --------"
t.printTree()


t.deleteNode(10)
print "------- Printing Tree after deleting node --------"
t.printTree()

t.deleteNode(1)
print "------- Printing Tree after deleting node --------"
t.printTree()
