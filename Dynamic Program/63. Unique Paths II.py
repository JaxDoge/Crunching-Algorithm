63. Unique Paths II


# Dynamic Programming
class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

		m = len(obstacleGrid)
		n = len(obstacleGrid[0])

		dp = [[0] * n for _ in range(m)]
		if obstacleGrid[0][0] == 0:
			dp[0][0] = 1

		for i in range(1, m):
			dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0

		for i in range(1, n):
			dp[0][i] = dp[0][i-1] if obstacleGrid[0][i] == 0 else 0

		for i in range(1, m):
			for j in range(1, n):
				dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0

		return dp[m-1][n-1]
				

class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])

		dp = [[0] * n for _ in range(m)]
		if obstacleGrid[0][0] == 0:
			dp[0][0] = 1

		for i in range(m):
			for j in range(n):
				if obstacleGrid[i][j] == 1:
					continue
				
				if i - 1 >= 0:
					dp[i][j] += dp[i - 1][j]
				
				if j - 1 >= 0:
					dp[i][j] += dp[i][j - 1]

		return dp[-1][-1]