# algo: push the last / rightmost character forward by finding a char that is smaller than it

# if found, put the rightmost char in the pos at which we found the 1st char smaller than it
# then fill the remaining chars from pos + 1 to end, by continiously selecting smallest first and putting it at the leftmost i.e. pos + 1 to end, then next smallest at pos + 2,... till len - 1

# if not found, meaning the last char was the smallest then try calling the same method (as for the full string with index len - 1) with str and len - 2

def find_smaller_char(c, str, i) : # i and to the left of i
  if str[i] < c:
    return i
  else:
    # if we did not find match, but we can go to the left
    if i != 0:
      return find_smaller_char(c, str, i-1)
    else: # did not find match and cannot go to the left
      return -1

def find_bigger(str):
  # put the following call in a loop !
  i = 1

  # sometimes during the phone interviews, having 1 extra var might be
  # the difference between a bug and no bug!

  # just have the extra var. and let the interviewer know
  x = len(str)-i

  # how long can we go on so that
  #

  ret = None
  while x >= 0 and ret == None:
    ret = bigger(str, x)

    if ret != None:
        print ret
        break

    i += 1
    x = len(str)-i

  if ret == None:
    print "no answer"        


# make the following a recursive method
# smallest value of k = 0
# largest value of k = len(str) - 1
def bigger(str, k):
  pos = -1
  index_from_right = len(str) - k
  print k-index_from_right


  while pos == -1:
    print k-index_from_right

    if k-index_from_right > -1:
      pos = find_smaller_char(str[k], str, k-index_from_right)

    index_from_right += 1

  # could not find the next larger string
  if pos == -1:
    #print "no answer"
    return None

  # initialize the new string to print
  new = []
  # fill new with zeros
  for z in xrange(len(str)):
    new.append(0)

  print "len of list new"
  print len(new)

  # if we have to put the unchanged characters to the left
  for j in xrange(pos):
    new[j] = str[j]
    print new[j]

  # put the rightmost / char at index 'k'
  print "pos"
  print pos

  print "k"
  print k

  print
  #print k
  #print index_from_right
  new[pos] = str[k]

  # now sort the rest of the characters after putting them in a list
  rem_chars = []

  # add the chars to the right of the lowest char we have found to the list to be sorted

  # fix this - there is a bug !
  for j in xrange(pos, len(str)):
    # the following if handles the case when
    if j != k:
        rem_chars.append(str[j])

  rem_chars.sort()

  new_index = pos + 1

  print "new_index"
  print new_index

  print "len of rem_chars"
  print len(rem_chars)

  for c in rem_chars:
    new[new_index] = c
    new_index += 1

  # print new
  return new


# test - 1
find_bigger("ab")
