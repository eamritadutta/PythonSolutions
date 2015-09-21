# level order traveral of a binary tree using a queue
import Queue

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

    def levelOrderTraversal(self):

        q = Queue.Queue()

        # put the root in the queue
        q.put(self.root)

        count = 1
        # don't know if root has any children or not
        next_count = 0

        values_in_level = ""

        # 1 approach to solve the level order traversal is to initially totally
        # forget about the fact we have to print an newline at the end of each
        # level and just try to print the whole tree correctly at first.
        while q.qsize() > 0:

            # take one from queue
            node = q.get()
            count -= 1
            values_in_level += str(node.val) + "->"

            if node.left != None:
                q.put(node.left)
                next_count += 1

            if node.right != None:
                q.put(node.right)
                next_count += 1

            # check if it is the last node in the level
            if count == 0:
                print values_in_level
                values_in_level = ""
                count = next_count
                next_count = 0

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

print "------- Printing Original Binary Search Tree --------"
t.printTree()

print "------- Level Order Traveral of Tree --------"
t.levelOrderTraversal()
