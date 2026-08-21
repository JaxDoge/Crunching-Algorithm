45. Jump Game II

# Regular DP
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n] * n
        dp[0] = 0

        for i in range(n):
            for j in range(nums[i] + 1):
                if i + j >= n:
                    break
                dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[-1]

# Greedy algorithm
# BFS
class Solution:
	def jump(self, nums: List[int]) -> int:
		n = len(nums)
		farthest = 0 # Find the end of next search range
		end = 0  # mark the end of one search range

		jump_cnt = 0

		for i in range(n-1):
			farthest = max(farthest, i+nums[i])
			if i == end:
				jump_cnt += 1
				end = farthest

		return jump_cnt