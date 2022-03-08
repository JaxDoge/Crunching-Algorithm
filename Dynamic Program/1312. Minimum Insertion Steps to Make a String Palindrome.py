1312. Minimum Insertion Steps to Make a String Palindrome


class Solution:
    def minInsertions(self, s: str) -> int:
    	n = len(s)
    	dp = [[0 for _ in range(n)] for _ in range(n)]

    	for i in range(n-1,-1,-1):
    		for j in range(i+1, n):
    			if s[i] == s[j]:
    				dp[i][j] = dp[i+1][j-1]
    			else:
    				dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

    	return dp[0][-1]
