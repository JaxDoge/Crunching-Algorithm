55. Jump Game


class Solution:
    def canJump(self, nums: List[int]) -> bool:
    	n = len(nums)
    	farthest = 0
    	for i in range(n-1):
    		farthest = max(farthest, i+nums[i])
    		# If there farthest index is behind or equal to current index
    		if farthest <= i:
    			return False

    	return farthest >= n-1