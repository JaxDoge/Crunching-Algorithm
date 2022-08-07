1004. Max Consecutive Ones III



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        l = r = 0
        while r < n:
            if nums[r] == 0:
                k -= 1
            r += 1

            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

        return r - l
