53. Maximum Subarray


# dp, dp[i] is the maxium subarray sum which end in nums[i]
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

# O(1) space complexity
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        dp_0 = nums[0]
        res = dp_0

        for i in range(1, n):
            dp_1 = max(nums[i], nums[i] + dp_0)
            res = max(res, dp_1)
            dp_0 = dp_1

        return res