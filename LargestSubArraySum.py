# This algorithm solves the task of finding the contiguous subarray with the largest sum within a one-dimensional array of numbers. If the numbers are all
# -ve then, the algorithm returns the smallest -ve number

def find_largest_sum(arr):

  if arr is None or len(arr) == 0:
      # this is like halting processing and throwing an exception in Java
      return "Invalid Input. Returning... "

  max_ending_here = arr[0]
  max_so_far = arr[0]


  # the following is to make sure that the for loop below, does not throw
  # any exceptions
  if len(arr) == 1:
      return max_so_far

  for n in arr[1:]:
      # new start (n) vs chain(n + max_ending_here)
      max_ending_here = max(n, n + max_ending_here)

      # what ever the decision is, its stored in max_ending_here
      # so comp that to the current max_so_far
      # and take the max
      max_so_far = max(max_so_far, max_ending_here)


  return max_so_far

# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [1, 2, -1, 2]

nums = [-2, -3, -1, -5]
print find_largest_sum(nums)
