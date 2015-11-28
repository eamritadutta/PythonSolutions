import heapq

def sortKSortedArr(arr, k):
    if arr is None or len(arr) <= 1:
        return arr

    # def the sorted arr to return
    ret = []

    # def the pri Q to use - len(priQ) = k + 1
    priQ = []

    # check each element of arr
    for n in arr:
        if len(priQ) <= k + 1:
            heapq.heappush(priQ, (n, "")) # don't need to values
        else:
            # get the min and put it in the return array
            ret.append(heapq.heappop(priQ)[0])
            heapq.heappush(priQ, (n, ""))

    while len(priQ) > 0:
        ret.append(heapq.heappop(priQ)[0])

    print ret
    return ret

# test code
sortKSortedArr([2, 6, 3, 12, 56, 8], 3)
