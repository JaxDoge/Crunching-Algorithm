712. Minimum ASCII Delete Sum for Two Strings

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
    	m = len(s1)
    	n = len(s2)

    	dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    	for col in range(1, n+1):
    		dp[0][col] = ord(s2[col-1]) + dp[0][col-1]
    	for row in range(1, m+1):
    		dp[row][0] = ord(s1[row-1]) + dp[row-1][0]

    	for row in range(1, m+1):
    		for col in range(1, n+1):
    			if s1[row-1] == s2[col-1]:
    				dp[row][col] = dp[row-1][col-1]
    			else:
    				dp[row][col] = min(dp[row-1][col]+ord(s1[row-1]), dp[row][col-1]+ord(s2[col-1]))

    	return dp[-1][-1]