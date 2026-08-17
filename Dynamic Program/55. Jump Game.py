55. Jump Game


class Solution:
	def canJump(self, nums: List[int]) -> bool:
		n = len(nums)
		furthest = 0
		for i in range(n - 1):
			# If we cann't even reach this index from previous positions
			if furthest < i:
				return False     
					   
			furthest = max(furthest, i + nums[i])


		return furthest >= n - 1