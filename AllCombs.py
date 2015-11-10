# the following code will print all combinations for the input array viz., 'A'

def printAllCombs(P):
    if P is None or len(P) == 0:
        print "Invalid Input. Returning."
        return

    # declare an array containing all zeros and increment
    A = [0 for _ in xrange(0, len(P))]

    # 000
    # 001
    # 010
    # 011
    # 100
    # 101
    # 110
    # 111

    # start scanning input array from left
    i = len(A) - 1

    while True:

        printCombination(P, A)

        # sets right most 0 to 1 and everything from right to the rightmost 0 to 0's. It always starts scanning from the right, so I don't need to pass any index!

        # all I need to do is to check the index that the call returns and make
        # sure that I discontinue when the returned index is negative (viz. -1)
        # since that means the array A now contains all 1's viz. 111 or 11111
        # and hence it is time to stop generating more permutations.
        i = setToRightmostZeroOne(A)

        if i < 0:
            break

def printCombination(P, A):

    l = []
    i = len(A) - 1
    # check each index from 0 to len(A) - 1
    while i >= 0:
        if A[i] == 1:
            l.append(P[i])
        i -= 1

    print l

# sets right most 0 to 1 and everything from right to the rightmost 0 to 0's
def setToRightmostZeroOne(A):

    # always start scanning from right !
    i = len(A) - 1

    # in each iteration we will try to decrement i
    while i >= 0:

        # check if 0, if 0, make 1
        if A[i] == 0:
            A[i] = 1
            return i

        else:
            A[i] = 0 # also continue in the loop

        i -= 1


    return i

# test code
printAllCombs([1, 2, 3])
