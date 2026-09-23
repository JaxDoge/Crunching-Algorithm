97. Interleaving String


# DFS
class Solution:
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		m = len(s1)
		n = len(s2)
		l = len(s3)
		if m + n != l:
			return False

		# Note the memo need to cover the memo[m][j] or memo[i][n] cases
		memo = [[-1] * (n + 1) for _ in range(m + 1)]

		def dfs(i, j):
			if i + j == l:
				return True
			
			if memo[i][j] > -1:
				return memo[i][j]

			res = 0
			if i < m and s1[i] == s3[i + j]:
				res = dfs(i + 1, j)
			
			# Note that we only need to fine one solution to return
			if res:
				return res

			# If the first path doesn't work, then res must be 0 (no change)
			if j < n and s2[j] == s3[i + j]:
				res = dfs(i, j + 1)

			memo[i][j] = res

			return res
		
		return dfs(0, 0) == 1