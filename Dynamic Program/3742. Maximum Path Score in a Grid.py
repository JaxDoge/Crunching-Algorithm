3742. Maximum Path Score in a Grid

# 3d DP
# For the cost 0 ... k, we find the maximum score for each of them
# Note the c represent the most possible cost to reach a grid, not the exact cost.

class Solution:
	def maxPathScore(self, grid: List[List[int]], k: int) -> int:
		n = len(grid)
		m = len(grid[0])

		dp = [[[float('-inf')] * (k + 1) for _ in range(m)] for _ in range(n)]
		dp[0][0][0] = 0

		for i in range(n):
			for j in range(m):
				for c in range(k + 1):
					# no path lead here
					if dp[i][j][c] == float('-inf'):
						continue

					# if we can move down
					if i + 1 < n:
						val = grid[i + 1][j]
						cost = 0 if val < 1 else 1
						if c + cost <= k:
							dp[i + 1][j][c + cost] = max(dp[i + 1][j][c + cost], dp[i][j][c] + val)

					# if we can move right
					if j + 1 < m:
						val = grid[i][j + 1]
						cost = 0 if val < 1 else 1
						if c + cost <= k:
							dp[i][j + 1][c + cost] = max(dp[i][j + 1][c + cost], dp[i][j][c] + val)



		ans = max(dp[-1][-1])

		return -1 if ans < 0 else ans