# 1 -> 2 -> 3
# 3 -> 2 -> 1
def revListR(head, prev): # 1, None

    # if last node
    if head.next == None:
        head.next = prev
        return head

    new_head = revListR(head.next, head) # 2, 1
    head.next = prev # 1 -> None

    return new_head

def reverseList(head):
    return revListR(head, None)

class Node():
    def __init__(self, v, n):
        self.val = v
        self.next = n

def printList(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next

    print vals

# test code
def test():

    n3 = Node(3, None)
    n2 = Node(2, n3)
    head = Node(1, n2)

    printList(head)
    new_head = reverseList(head)
    printList(new_head)

# call test code
test()
