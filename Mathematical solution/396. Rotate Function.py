396. Rotate Function



# find the patten
# from the second rotation, the F(k) = F(k - 1) - nums[n - k] * (n - 1) + (sum - nums[n - k]) 
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sumup = sum(nums)
        F0 = sum(idx * num for idx, num in enumerate(nums))
        ans = F0

        for k in range(1, n):
            Fk = F0 - nums[n - k] * n + sumup
            ans = max(ans, Fk)
            F0 = Fk

        return ans