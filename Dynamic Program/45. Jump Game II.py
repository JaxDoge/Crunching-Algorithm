45. Jump Game II


# Greedy algorithm
class Solution:
    def jump(self, nums: List[int]) -> int:
    	n = len(nums)
    	farthest = 0
    	end = 0  # mark the end of one search range

    	jump_cnt = 0

    	for i in range(n-1):
    		farthest = max(farthest, i+nums[i])
    		if i == end:
    			jump_cnt += 1
    			end = farthest

    	return jump_cnt