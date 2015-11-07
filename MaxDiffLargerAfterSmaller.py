def printMaxDiff(nums):
    if nums == None or len(nums) == 0:
        print "Invalid input array of numbers."
        return

    smallest_index = 0
    largest_index = 0

    maybe_smallest_index = None
    max_diff = -1

    # i will range from 1 to len(nums) - 1
    for i, num in enumerate(nums):

        print "Currently scanning index: " + str(i) + " with value: " + str(num)

        if num < nums[smallest_index] and maybe_smallest_index is None:

            maybe_smallest_index = i
            print "maybe_smallest_index: " + str(i)

        elif num < nums[smallest_index] and maybe_smallest_index is not None and num < nums[maybe_smallest_index]:

            maybe_smallest_index = i
            print "maybe_smallest_index: " + str(i)

        elif num > nums[largest_index]:

            if maybe_smallest_index == None:
                largest_index = i
                max_diff = nums[largest_index] - nums[smallest_index]

                print "Assigning largest_index as: " + str(i)
                print "Max diff: " + str(max_diff)


            else: # maybe_smallest_index is not None:
                diff = num - nums[maybe_smallest_index]

                print "diff: " + str(diff)

                if diff > max_diff:
                    max_diff = diff
                    smallest_index = maybe_smallest_index
                    largest_index = i

    if max_diff is not None:
        print "The max diff in the input array: " + str(nums) + " is: " + str(max_diff)

    else:
        print "The max diff in the input array: " + str(nums) + " is None."

# test code
printMaxDiff([7, 9, 5, 6, 3, 2])

printMaxDiff([2, 3, 10, 6, 4, 8, 1])

printMaxDiff([1, 2, 6, 80, 100])

printMaxDiff([80, 2, 6, 3, 100])

printMaxDiff([1, 2, 3, 4, 5])

printMaxDiff([5, 4, 3, 2, 1])

printMaxDiff([5, 5, 5, 5, 5])
