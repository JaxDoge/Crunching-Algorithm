516. Longest Palindromic Subsequence

# two pointers
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
    	# use two pointers i, j to iterate the whole string from opposite directions
    	# use dp table to record the result of subsequence s[i:j+1]
    	# i <= j
    	# the result of statu s[i:j+1] = dp[i][j] could be derived from other status
    	# if s[i] == s[j], dp[i][j] = dp[i+1][j-1]+2
    	# else dp[i][j] = max(dp[i+1][j], dp[i][j-1]) since s[i] and s[j] won't appear in one palindromic subseqence
    	# when i == j, dp[i][j] = 1, which is the base case
    	m = len(s)

    	dp = [[0 for _ in range(m)] for _ in range(m)]

    	# base case, 
    	for i in range(m):
    		dp[i][i] = 1

    	for i in range(m-2, -1, -1):
    		for j in range(i+1,m):
    			if s[i] == s[j]:
    				dp[i][j] = dp[i+1][j-1]+2
    			else:
    				dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    	return dp[0][-1]
