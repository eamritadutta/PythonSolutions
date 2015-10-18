# Jump Game:
# Given an array start from the first element and reach the last by jumping. The jump length can be at most the value at the current position in the array. Optimum result is when u reach the goal in minimum number of jumps.
#
# For ex:
# Given array A = {2,3,1,1,4}
# possible ways to reach the end (index list)
# i) 0,2,3,4 (jump 2 to index 2, then jump 1 to index 3 then 1 to index 4)
# ii) 0,1,4 (jump 1 to index 1, then jump 3 to index 4)
#
# Since second solution has only 2 jumps it is the optimum result.

import sys

def findMinJumps(arr, st, min_jumps):

    # base case - not acceptable
    if st >= len(arr):
        return sys.maxint

    # number of jumps can only be 0 or +ve
    if min_jumps[st] != -1:
        return  min_jumps[st]

    # base case - when we have reached the last cell
    if st == len(arr) - 1:
        min_jumps[st] = 0
        return 0

    # check starting from # of jumps = value in cell
    num_jumps = arr[st]
    min_jump = sys.maxint

    while  num_jumps > 0:

        jump = 1 + findMinJumps(arr, st + num_jumps, min_jumps)

        if jump < min_jump:
            min_jump = jump

        num_jumps -= 1

    min_jumps[st] = min_jump

    # if st == 0:
    #     print "Min. # of jumps is: " + str(min_jumps[0])

    return min_jump


# test code
# print findMinJumps([2, 3, 1, 1, 4], 0, [-1, -1, -1, -1, -1])

# print findMinJumps([1, 3, 6, 1, 0, 9], 0, [-1, -1, -1, -1, -1, -1])

# print findMinJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 0, [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

# test code for edge cases
# print findMinJumps([0], 0, [-1])

print findMinJumps([5, 4, 3, 2], 0, [-1, -1, -1, -1])
