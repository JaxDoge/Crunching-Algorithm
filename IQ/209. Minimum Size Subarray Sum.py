209. Minimum Size Subarray Sum



# Prefix sum array
# find the first subarray (or a number, which is the final answer)
# fix the array length and slide the window advance
# try to shrink the left end, if it is possible 
# return the length of the window when the right end is n - 1
# Note that in some point the sum of elements in the window may less than target, but that is Ok
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        l = r = 0
        window = 0
        while r < n + 1:
            if prefix[r] - prefix[l] >= target:
                window = r - l
                break
            r += 1

        # badcase 1, cannot find the subarray
        if not window:
            return 0

        while r < n + 1:
            # try to shrink the the left end
            while prefix[r] - prefix[l] >= target:
                # update window length if possible
                window = r - l
                l += 1

            # At here, ths sum in the window is less than the target, so we move window forward
            # until it larger than target or out of bound
            l += 1
            r += 1

        return window


    