583. Delete Operation for Two Strings

# dp table
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    	m = len(word1)
    	n = len(word2)

    	dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    	# base case
    	for col in range(1, n+1):
    		dp[0][col] = col
    	for row in range(1, m+1):
    		dp[row][0] = row

    	for row in range(1, m+1):
    		for col in range(1, n+1):
    			if word1[row-1] == word2[col-1]:
    				dp[row][col] = dp[row-1][col-1]
    			else:
    				dp[row][col] = min(dp[row-1][col]+1, dp[row][col-1]+1)

        return dp[-1][-1]