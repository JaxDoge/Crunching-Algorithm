1143. Longest Common Subsequence

# dp dfs 自顶向下拆分
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    	m = len(text1)
    	n = len(text2)
    	memo = [[-1 for _ in range(n)] for _ in range(m)]

    	def dp(i,j):
    		nonlocal text1, text2, m, n
    		# base case, no common substring
    		if i == m or j == n:
    			return 0

    		if memo[i][j] != -1:
    			return memo[i][j]

    		if text1[i] == text2[j]:
    			memo[i][j] = 1+dp(i+1, j+1)
    		else:
    			memo[i][j] = max(dp(i+1,j),dp(i,j+1)) # 注意 i+1 j+1 的情况已经被覆盖了，不必写出
    			# 计算s1[i+1..]和s2[j+1..]的lcs长度，这个长度肯定是小于等于s1[i..]和s2[j+1..]中的lcs长度的

    		return memo[i][j]

    	return dp(0, 0)


# dp table 自底向上
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    	m = len(text1)
    	n = len(text2)
    	dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    	# 遍历内表
    	for i in range(1, m+1):
    		for j in range(1, n+1):
    			if text1[i-1] == text2[j-1]:
    				dp[i][j] = dp[i-1][j-1] + 1
    			else:
    				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


