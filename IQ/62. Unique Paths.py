62. Unique Paths


from math import comb
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		return comb(m + n - 2, n - 1)



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
        
        return dp[m - 1][n - 1]