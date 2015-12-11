def mergeSortedLists(l1, l2):
    p1 = 0
    p2 = 0

    sortedl = []

    while p1 < len(l1) and p2 < len(l2):

        if l1[p1] > l2[p2]:
            sortedl.append(l2[p2])
            p2 += 1
        else:
            sortedl.append(l1[p1])
            p1 += 1

    # print sortedl
    # print p1
    # print p2

    if p1 == len(l1):
        # print "p2: " + str(p2)
        # print "val: " + str(len(l2) - 1)
        while p2 <= (len(l2) - 1):
            #print "inc p2"
            sortedl.append(l2[p2])
            p2 += 1

    if p2 == len(l2):
        # print "p1: " + str(p1)
        # print "val: " + str(len(l1) - 1)
        while p1 <= (len(l1) - 1):
            #print "inc p1"
            sortedl.append(l1[p1])
            p1 += 1

	print sortedl
    return sortedl


mergeSortedLists([1], [3,4])
mergeSortedLists([1,2], [3])
mergeSortedLists([1,2], [])
mergeSortedLists([], [3,4])
mergeSortedLists([], [])
mergeSortedLists([1,2], [3,4])
