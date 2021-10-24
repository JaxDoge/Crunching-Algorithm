416. Partition Equal Subset Sum


# dp table
# the problem could transform to: if there is a subset of nums that the sum of elements is equal to sum(nums)/2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
    	if sum(nums) % 2 != 0:
    		return False

    	target = sum(nums) // 2
    	length = len(nums)

    	dp = [[False for _ in range(target+1)] for _ in range(length+1)]

    	# base case
    	for row in range(0, length+1):
    		dp[row][0] = True

    	for row in range(1, length+1):
    		for col in range(1, target+1):
    			# 装不下第 row 个数
    			if col < nums[row-1]:
    				dp[row][col] = dp[row-1][col]
    			else:
    				dp[row][col] = dp[row-1][col] or dp[row-1][col-nums[row-1]]
    	return dp[-1][-1]


# dp table compress

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
    	if sum(nums) % 2 != 0:
    		return False

    	target = sum(nums) // 2
    	length = len(nums)
    	dp = [False for _ in range(target+1)]
    	dp[0] = True

    	for row in range(nums):
    		for col in range(target, 0, -1):
    			if col >= nums[row]:
    				dp[col] = dp[col] or dp[col-nums[row]]
    	return dp[-1]