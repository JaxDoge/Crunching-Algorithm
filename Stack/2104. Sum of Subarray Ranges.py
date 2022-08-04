2104. Sum of Subarray Ranges

# Amazon intern OA
# monotonic stack
# We want to find the sum of minimum from all subarray
# and the sum of maximum.
# Because we need specify a index as the min or max, we need define that if nums[i] == nums[j], nums[i] is closer to min and nums[j] is closer to max, since i < j
# for a given index i, the number of subarray that has the minimum nums[i] could be calculate
# fistrly, the first number small than nums[i] at LHS is nums[j], and the one at RHS is nums[k]
# Secondly, the subarray of [j + 1,..,i,..,k-1] that including nums[i] is combined from two parts
# the first part could be [i], [i-1, i] .. [j + 1,..,i], totally (i - j) possibilities
# the second part could be [], [i + 1], [i + 1, i + 2] .. [i + 1,..,k - 1], totally (k - i) possibilities
# In the end, the number of subarray that including nums[i] is (i - j) * (k - i)
# we could use monotonic stack to locate the j and k for each i (to find closest larger or smaller, always turn to this)
# In the same way, we could find the sum of all maximum of all subarray

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        # loop from left to right
        minLeft = [0] * n
        maxLeft = [0] * n
        minStack = []
        maxStack = []

        for i, num in enumerate(nums):
            # Note that if index is 0, the minleft and maxleft set to -1, thus the first part would be i + 1
            while minStack and nums[minStack[-1]] > num:
                minStack.pop()
            minLeft[i] = minStack[-1] if minStack else -1
            minStack.append(i)

            # By our definition, == is smaller
            while maxStack and nums[maxStack[-1]] <= num:
                maxStack.pop()
            maxLeft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)

        minRight = [0] * n
        maxRight = [0] * n
        minStack = []
        maxStack = []

        for i in range(n - 1, -1, -1):
            num = nums[i]
            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop() 
            maxRight[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)

        minSum = maxSum = 0
        for i in range(n):
            num = nums[i]
            minsubCount = (i - minLeft[i]) * (minRight[i] - i)
            minSum += minsubCount * num

            num = nums[i]
            maxsubCount = (i - maxLeft[i]) * (maxRight[i] - i)
            maxSum += maxsubCount * num

        return maxSum - minSum


