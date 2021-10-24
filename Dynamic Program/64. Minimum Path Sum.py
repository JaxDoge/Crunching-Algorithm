64. Minimum Path Sum


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
    	rows = len(grid)
    	cols = len(grid[0])

    	dp = [[0 for _ in range(cols)] for _ in range(rows)]

    	# base case

    	dp[0][0] = grid[0][0]

    	for row in range(1, rows):
    		dp[row][0] = dp[row-1][0] + grid[row][0]

    	for col in range(1, cols):
    		dp[0][col] = dp[0][col-1] + grid[0][col]

    	for row in range(1, rows):
    		for col in range(1, cols):
    			dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]

    	return dp[-1][-1]
