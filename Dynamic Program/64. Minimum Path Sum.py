64. Minimum Path Sum


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # DP
        dp = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue

                if i > 0:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i - 1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i][j - 1])
        
        return dp[-1][-1]
