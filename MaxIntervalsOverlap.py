# -*- coding: utf-8 -*-

# From GeeksforGeeks
# Find the point where maximum intervals overlap
# Consider a big party where a log register for guest’s entry and exit times is # maintained. Find the time at which there are maximum guests in the party. Note # that entries in register are not in any order.

# Input: arrl[] = {1, 2, 10, 5, 5}
#        exit[] = {4, 5, 12, 9, 12}

# First guest in array arrives at 1 and leaves at 4,
# second guest arrives at 2 and leaves at 5, and so on.

# Output: 5
# There are maximum 3 guests at time 5.

# Just defining a function and getting on with it

def maxIntervalOverlap():

    # hard coding the input arrays for now
    entry = [1, 2, 10, 5, 5]
    exit = [4, 5, 12, 9, 12]

    # find the min in 'entry' array
    min = 25
    for val in entry:
        if val < min:
            min = val

    # min = 1
    print "min: " + str(min)

    # find the max in the 'exit' array
    max = 0
    for val in exit:
        if val > max:
            max = val

    # max = 12
    print "max: " + str(max)

    # max - min = 11
    # declare an array to keep track of # of guests present in each hour
    # size of the array = 11

    # so if we declare an array of size 11
    # st index of array = 0
    # end index of array = 10

    stat = [0] * (max + 1) # since index starts from 0

    # now traverse entry and  exit and populate 'stat'
    for st, end in zip(entry, exit): # st = 2, end = 5
        # st = 1 => stat[st] += 1
        for i in xrange(st, end+1): # in xrange 2, 5 => 2, 3, 4

            stat[i] += 1
    # now iterate stat and find max of stat

    # find the max in the 'exit' array
    max = 0
    for val in stat:
        if val > max:
            max = val

    # max = 12
    print "max # of guests were present at: " + str(max)



maxIntervalOverlap()
