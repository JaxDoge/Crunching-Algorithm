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
    	if not nums:
    		return 0
    	length = len(nums)
    	dp_0 = nums[0]
    	res = float('-inf')

    	for index in range(1, length):
    		dp_1 = max(nums[index], dp_0+nums[index])
    		res = max(res, dp_1)
    		dp_0 = dp1

    	return res