152. Maximum Product Subarray


# kadane's algorithm
# Note that we need another dp table minDP to record the minimum product of subarray end with nums[i-1]
# Because nums[i] could be negative, thus it could get a largest value with the minimum values 
class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		n = len(nums)
		if n < 2:
			return nums[0]

		maxDP = [nums[0]]
		minDP = [nums[0]]
		for i in range(1, n):
			maxI = max(maxDP[i - 1] * nums[i], minDP[i - 1] * nums[i], nums[i])
			minI = min(maxDP[i - 1] * nums[i], minDP[i - 1] * nums[i], nums[i])
			maxDP.append(maxI)
			minDP.append(minI)

		return max(maxDP)


# I got it
class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		n = len(nums)
		dp_max = [float('-inf')] * (n)
		dp_min = [float('inf')] * (n)

		dp_max[0] = nums[0]
		dp_min[0] = nums[0]

		for i in range(1, n):
			dp_max[i] = max(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
			dp_min[i] = min(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
		
		return max(dp_max)

