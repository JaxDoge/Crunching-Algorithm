1984. Minimum Difference Between Highest and Lowest of K Scores




# if K > 1, we only need to find the lowest and highest scores in nums
# bucket sort
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k < 2 or n < 2:
            return 0

        if k >= n:
            return max(nums) - min(nums)

        nums.sort()
        ans = float("inf")
        for i in range(k - 1, n):
            pre = nums[i - k + 1]
            nex = nums[i]
            if nex - pre < ans:
                ans = nex - pre
                if ans == 0:
                    return ans

        return ans





        
