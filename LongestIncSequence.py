# The following algorithm returns the length of longest increasing sequence in a input array in O(N log N) time

# first I am trying to reason about the problem on lines similar to the explanation at GeeksForGeeks

# lets start with the input array:
# A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

# to solve the problem in O(N log N) time, we need another array to keep
# track of the end indices of increasing sequences (of unique length)

# In the end, the length of B is the length of the longest increasing sequence in A

# for the sake of clarity in explanation, I will have more than one array below

# scan A[0] and put it in B[0]

# now scan A[1] = 8
# search for 8 in B. the index 1 will be returned since 8 > 0
# B[1] = 8
# B = [0, 8]

# now scan A[2] = 4
# search for 4 in B
# the index 1 will be returned
# B[1] = 4
# B = [0, 4]

# now scan A[3] = 12
# search for 12 in B
# the index 2 will be returned
# B[2] = 12
# B = [0, 4, 12]

# now scan A[4] = 2
# search for 2 in B
# the index 1 will be returned
# B[1] = 2
# B = [0, 2, 12]

# now scan A[5] = 10
# search for 10 in B
# the index 2 will be returned
# B[2] = 10
# B = [0, 2, 10]

# A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# now scan A[6] = 6
# search for 6 in B
# the index 2 will be returned
# B[2] = 6
# B = [0, 2, 6]

# now scan A[7] = 14
# search for 14 in B
# the index 3 will be returned
# B[3] = 14
# B = [0, 2, 6, 14]

def findElementInArray(s, B, st, end): # 0  2  B=[0, 4, 12] s=2
    # stop when end < st
    # at this point we have to return an index which will be the appropriate
    # position for 's' in B
    if end < st:
        return st

    mid = st + ((end - st + 1) / 2) # 0
    # this should never happen in this problem, if all the elements in the
    # input array are unique
    if s == B[mid]: # B[mid] = 4
        return mid
    elif s > B[mid]:
        return findElementInArray(s, B, mid + 1, end) # 1  0
    else:
        return findElementInArray(s, B, st, mid - 1) # 0  0

def printLenOfLis(A):
    # sanity check
    if len(A) == 0 or A is None:
        print "Invalid input array"
        return

    # scan A[0] and put it as the first element of B
    B = [A[0]]

    # scan A starting from the index 1
    for i in xrange(1, len(A)):

        # search for A[i] in B by calling a recursive method
        ins = findElementInArray(A[i], B, 0, len(B) - 1)
        if ins == len(B):
            B.append(A[i])
        else: # ins < len(B). Note: ins can never be > len(B)
            # overwrite
            B[ins] = A[i]

    print "The length of the LIS in " + str(A) + " is: " + str(len(B))

# test code - Example is from wikipedia
printLenOfLis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
