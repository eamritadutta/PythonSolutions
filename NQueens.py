# the following algorithm prints all non - conflicting configurations of placing N queens on a N x N chess board

import time

valid_perms = 0

def printNonConflictingConfigs(N):

    global valid_perms

    # array for storing the column position of queen in each row
    # -1 indicates that
    C = [-1] * N

    for val in xrange(0, N):
        C[val] = val

    # now permute the values in 'C'
    perm(C, N, 0)

    print "Number of non-conflicting positions for " + str(N) + " queens are: " + str(valid_perms)

# prints all permuatations of numbers between 0 and N - 1
# def printPerms(N):
#
#     # first declare an array to contain values from 0 to N - 1
#     vals = [-1] * N
#
#     for val in xrange(0, N):
#         vals[val] = val
#
#     perm(vals, N, 0)


def perm(vals, N, curr_index):

    global valid_perms

    # print "curr_index: " + str(curr_index)

    if curr_index == N - 1:
        # print the valid non-conflicting configuration of chess board for
        # placing the n queens
        if isConflict(vals) == False:
            valid_perms += 1
            print vals

        return

    # number of rations at 'curr_index' = N - curr_index
    for i in xrange(N - curr_index): #  => for 0, i = [0, 1, 2]

        # call for printing other permuatations
        perm(vals, N, curr_index + 1) # vals, 3, 2

        # rotate
        temp = vals[curr_index] # temp = vals[0] = 0
        # print "temp: " + str(temp)

        for j in xrange(curr_index, N-1): # 1, 2 # one time
            # print "j: " + str(j)
            vals[j] = vals[j+1]  # vals[1] = vals[2]

        vals[N-1] = temp # vals[2] = vals[curr_index]
        # print "after rotation: " + str(vals)

# Assuming queen A is at (i, j) and queen B is at (k, l), then
# abs(i - k) == abs(j - l)
def isConflict(vals):

    # check that for each val and index in vals, the value
    # abs(val - index) in unique

    for i in xrange(len(vals)):
        for j in xrange(i+1, len(vals)):
            if abs(i - j) == abs(vals[i] - vals[j]):
                return True

    return False

# printPerms(3) # all perms of 0, 1, and 2
start_time = time.time()
printNonConflictingConfigs(5)
print "Time taken: " + str(time.time()-start_time)
