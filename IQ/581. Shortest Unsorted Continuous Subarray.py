581. Shortest Unsorted Continuous Subarray


# Double pointers
# The key point is, in the disordered segment, the begin element is always larger than the
# minimum value (in the segment), and the end element is always smaller than the maximum value
# So we could maintain a varible max that represent the maximum of nums[:i],
# and if current element is smaller than max, it could be the end of disordered segment
# Same as the beginning of the segment, but we loop from the end of nums

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # if end and start are untounched, we should return 0
        # great trick!
        end = -1
        start = 0

        maxNow = float("-inf")
        minNow = float("inf")

        for i in range(n):
            # find the end point, at least a candidate
            if nums[i] < maxNow:
                end = i
            else:
                maxNow = nums[i]

            if nums[n - i - 1] > minNow:
                start = n - i - 1
            else:
                minNow = nums[n - i - 1]

        return end - start + 1



# Monotonic Stack
# Wrong !
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        mstack = []
        start = end = -1
        for idx, num in enumerate(nums):
            if mstack and num < mstack[-1][1]:
                end = idx
                # if the nums[idx + 1] == num, end need move right by 1
                tmpIdx = idx
                while tmpIdx < n - 1 and nums[tmpIdx + 1] == num:
                    end += 1
                    tmpIdx += 1 

            while mstack and num < mstack[-1][1]:
                startC, _ = mstack.pop()
                if start != -1 and startC < start:
                    start = startC
            mstack.append((idx, num))

        if start == -1:
            return 0

        return end - start + 1

# 
