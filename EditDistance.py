# This is a typical dynamic programming problem

# e.g. strings
# abcd
# abd

# assuming all operations to be of the same cost

str1 = "abcd"
str2 = "abed"

# now define an edit distance function and then call it from below

def edit_distance(str1, str2):

    print "str1: " + str1 + ", str2: " + str2

    # base case 1
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return 0

    # base case 2
    if len(str1) == 1 and len(str2) == 1 and str1 != str2:
        return 1

    # base case 3
    if len(str1) == 0 and len(str2) == 0:
        print "len(str1) == 0 and len(str2) == 0"
        return 0

    if len(str1) == 0:
        return len(str2)

    if len(str2) == 0:
        return len(str1)

    if str1[0] != str2[0]:

        return 1 + min(edit_distance(str1[1:], str2[:]), edit_distance(str1[:], str2[1:]), edit_distance(str1[1:], str2[1:]))

    else:
        # the following is a 0 cost operation
        return edit_distance(str1[1:], str2[1:])


print edit_distance(str1, str2)
