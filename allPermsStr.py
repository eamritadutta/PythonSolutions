def allPerms(istr):
    # list to operate on
    l = []
    for s in istr:
        l.append(s)
    perms = []
    allPermsR(l, 0, perms)
    return perms

def allPermsR(istr, ci, perms): # is = "xy", ci = 1
    if not istr:
        return set()
    # check ci
    if ci == len(istr) - 1: # 0 == 1
        #print istr
        to_return = ""
        for s in istr:
            to_return = to_return + s
        perms.append(to_return)
        return

    numRots = ci

    # rotate len(is) times
    while True:

        if numRots >= len(istr):
            break

        # swap char at index ci w/ ci, then ci + 1, ci + 2 and ci + 3 (3 == len(is) - 1)
        t = istr[ci]
        istr[ci] = istr[numRots]
        istr[numRots] = t

        # call all Perms recur for smaller lengths viz. i + 1
        allPermsR(istr, ci + 1, perms)

        # swap back
        t = istr[ci]
        istr[ci] = istr[numRots]
        istr[numRots] = t

        numRots += 1


#ret = allPerms("abcd")
#ret = allPerms("abc")
ret = allPerms("ab")
print ret
