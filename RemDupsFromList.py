# class for node
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# create the following list inside a method
# 1->1->2->3->3
def create_list():
    three_one = Node(3, None)
    three_two = Node(3, three_one)
    two = Node(2, three_two)
    one_one = Node(1, two)
    head = Node(1, one_one)

    return head

def rem_dups(head):
    # base case; head == None
    if head == None:
      return None

    n = head

    while n != None and n.val == head.val:
      n = n.next

    head.next = n
    rem_dups(head.next)

    return head

def print_list(head):
    while head != None:
        print str(head.val) + "->"
        head = head.next

head = create_list()
print "Input list with duplicates: "
print_list(head)
new_head = rem_dups(head)
# new_head = rem_dups(None)
print 
print "De-duped list: "
print_list(new_head)
