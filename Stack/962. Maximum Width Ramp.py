962. Maximum Width Ramp



class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stkI = []

        for idx, num in enumerate(nums):
            if not stkI or nums[stkI[-1]] > num:
                stkI.append(idx)

        res = 0
        for j in range(n - 1, -1, -1):
            # we don't have to worry about the situation j < i, because j - i would less than Zero, but res always beyong 0
            while stkI and nums[j] >= nums[stkI[-1]]:
                res = max(res, j - stkI[-1])
                stkI.pop()

        return res   