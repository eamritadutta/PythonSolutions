#         10
#     5        15
# 1     7   13    25

# pre : 10  5  1  7  15  13  25 #
# in:     1  5   7  10  13  15  25  # 10's ind = 3, 1's = 0; 3 - 0 = 3; 25's = 6; 6 - 3 = 3

# class for tree node
class Node:
  # constructor
  def __init__(self, val, left, right):
      self.val = val
      self.left = left
      self.right = right

# can't use bin search since in might not be sorted
def find_in_inorder(ino, num, stin, endin):

    print "find_in_inorder called with ino as: {}, num as: {}, stin as {} and endin as: {}".format(str(ino), num, stin, endin)

    k = stin
    while k <= endin:
        if ino[k] == num:
            return k
        k += 1

    return -1

# 1st call will have st = 0 and end = len(pre) - 1
def reconstruct(stp, endp, pre, stin, endin, ino):

    # base case
    if stp > endp or stin > endin or stp < 0 or endp >= len(pre):
        return None

    # root = pre[left_most]
    print "trying to access pre[stp] " + str(stp)
    n = Node(pre[stp], None, None)

    # find the value n in in
    index_in_in = find_in_inorder(ino, n.val, stin, endin)

    # the following check is very imp since the array in might not contain n
    # this would be a case of invalid input
    if index_in_in == -1:
      print "The 2 input arrays do not represent the same tree. Returning without creating the tree"
      return None

    # break pre and make 2 recursive calls
    num_eles_left = index_in_in - stin

    # left sub-tree
    # check before calling!
    left_n = reconstruct(stp + 1, stp + num_eles_left, pre, stin, index_in_in - 1, ino)

    # right sub-tree
    # check before calling!
    r_n = reconstruct(stp + num_eles_left + 1, endp, pre, index_in_in, endin, ino)

    n.left = left_n
    n.right = r_n

    return n


# test the method
ino = [4, 2, 5, 1, 6, 3]
pre = [1, 2, 4, 5, 3, 6]

n = reconstruct(0, 5, pre, 0, 5, ino)
print n.val
