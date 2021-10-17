72. Edit Distance


# dfs + memo, 双指针
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    	m = len(word1)
    	n = len(word2)

    	memo = dict()
    	def dfs(i, j):
    		if (i, j) in memo:
    			return memo[(i, j)]
    		# base case
    		if i < 0:
    			return j+1
    		if j < 0:
    			return i+1

    		if word1[i] == word2[j]: # 无操作
    			memo[(i, j)] = dfs(i-1, j-1)
    		else:  # 无非三种可能操作 插入，删除，替换
    			memo[(i, j)] = min(dfs(i, j-1)+1, dfs(i-1, j)+1, dfs(i-1,j-1)+1)
    		return memo[(i, j)]
    	return dfs(m-1, n-1)


# dp table
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    	m = len(word1)
    	n = len(word2)

    	dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    	# base case
    	for i in range(m+1):
    		dp[i][0] = i
    	for j in range(n+1):
    		dp[0][j] = j

    	for i in range(1, m+1):
    		for j in range(1, n+1):
    			if word1[i] == word[j]:
    				dp[i][j] = dp[i-1][j-1]
    			else:
    				dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    	return dp[-1][-1]

    

