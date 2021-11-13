877. Stone Game

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
    	n = len(piles)
    	dp = [[list() for _ in range(n)] for _ in range(n)]

    	for i in range(n):
    		dp[i][i] = [piles[i], 0]

    	for i in range(n-2, -1, -1):
    		for j in range(i+1, n):
    			first = max(piles[i]+dp[i+1][j][1], piles[j]+dp[i][j-1][1])
    			second = sum(piles[i:j+1]) - first
    			dp[i][j] = [first, second]

    	return dp[0][n-1][0] > dp[0][n-1][1]

