# Say there are N stairs and we can climb either 1 or 2 stairs at a time, so what is the total number of possible ways of reaching Nth stair ?
#
# Start with a very small example and try to find a pattern / or find a data structure which can help us solve the problem.
#
# Looks like with trying out only 1 small example is of NO help. So, try out a series of examples viz., for N = 1, N = 2, N = 3 and so on.. Do for 5 such consecutive N’s and see if you can find the pattern. Remember, here we are only looking for total # of ways to reach the Nth stair for each N.
#
# say N = 1
# 1st way = 1
#
# Total # of ways = 1
#
# say N = 2
# 1st way = 1, 1
# 2nd way = 2
#
# Total # of ways = 2
#
# say N = 3
#
# 1st way = 1, 1, 1
# 2nd way = 1, 2
# 3rd way = 2, 1
#
# Total # of ways = 3
#
# say N = 4
#
# 1st way = 1, 1, 1, 1
# 2nd way = 1, 1, 2
# 3rd way = 1, 2, 1
# 4th way = 2, 1, 1
# 5th way = 2, 2
#
# Total # of ways = 5
#
# say N = 5
#
# 1st way = 1, 1, 1, 1, 1
# 2nd way = 1, 1, 1, 2
# 3rd way = 1, 1, 2, 1
# 4th way = 1, 2, 1, 1
# 5th way = 2, 1, 1, 1
# 6th way = 1, 2, 2
# 7th way = 2, 1, 2
# 8th way = 2, 2, 1
#
# Total # of ways = 8
#
# If after this, I cannot see the series for 1, 2, 3, 5, 8 then I don’t deserve a computer engineering job!
#
# Now try to code it up by modifying the actual fibonacci series generation algorithm so that the algorithm starts storing in an array and returns the final value for any given N
#
# any N less than 1 should be discarded
#
# for N = 5 we need to have an array of size 5 and return the value at a[4]
# for N = 6 we need to have an array of size 6 and return the value at a[5]
#
# Now the question is how do we calculate the contents at each a[i] for i = 0 to N -1

def find_num_ways_to_climb(n):
  # sanity check - remember lowest val of n is 1
  if n < 1:
    # print "Number of stairs to climb cannot be negative or zero. Stopping to process."
    return None

  # create an array of size n
  steps = [0] * n # will range from 0 to n - 1

  # now to calculate value in steps[i] we need the value of steps[i - 1] and steps[i - 2] (unless i == 0 or i == 1). Hence, the i will be increasing (I am mentioning this because there might be cases of dynamic programming where if we use a decreasing i that will ease the generation of a solution).


  for i in xrange(0, n): # 0 to n - 1

    # base case 1
    if i == 0:
      steps[i] = 1
      continue

    # base case 2
    if i == 1:
      steps[i] == 2
      continue

    steps[i] = steps[i - 1] + steps[i - 2]

  # at the end of the iteration of the for loop, we have our required result in steps[n - 1]
  return steps[n - 1]


# following are a bunch of test cases
print "Number of ways to climb -2 stairs is: " + str(find_num_ways_to_climb(-2))
print "Number of ways to climb 0 stairs is: " + str(find_num_ways_to_climb(0))
print "Number of ways to climb 1 stairs is: " + str(find_num_ways_to_climb(1))
print "Number of ways to climb 1 stairs is: " + str(find_num_ways_to_climb(1))
print "Number of ways to climb 15 stairs is: " + str(find_num_ways_to_climb(15))
