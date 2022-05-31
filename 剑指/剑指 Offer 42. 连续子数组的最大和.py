剑指 Offer 42. 连续子数组的最大和


# Prefix sum
# rolling out sumup list rSum that rSum[i] = sum(nums[0:i]), rSum[0] = 0
# then we could calculate sum(nums[i:j]) from rSum[j] - rSum[i]
# maintain min list that: min[i] = min(rSum[0:i+1])
# calculate the subMax list that subMax[i] = rSum[i] - min[i]
# the maximum of subMax list is the answer we want
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        rSum = [0] * (n + 1)
        for i in range(n):
            rSum[i + 1] = rSum[i] + nums[i]

        minSum = [0]
        for i in range(1, n + 1):
            minSum.append(min(minSum[i - 1], rSum[i]))

        subMax = []
        for i in range(n):
            subMax.append(rSum[i + 1] - minSum[i])

        return max(subMax)

# Or DP
# dp[i] is the maxium subarray sum which end in nums[i]
# so the maximum sum of subarray is max(dp)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [0]*length
        dp[0] = nums[0]

        for index in range(1, length):
            dp[index] = max(nums[index], dp[index-1]+nums[index])

        return max(dp)