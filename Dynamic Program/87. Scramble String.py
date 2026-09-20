87. Scramble String

# Direct DFS
class Solution:
	def isScramble(self, s1: str, s2: str) -> bool:
		from functools import cache

		@cache
		def dfs(i, j, length):
			a = s1[i:i+length]
			b = s2[j:j+length]

			if a == b:
				return True
			
			if Counter(a) != Counter(b):
				return False

			for k in range(1, length):
				if (
					dfs(i, j, k) and
					dfs(i+k, j+k, length - k)
				):
					return True

				if (
					dfs(i, j + length - k, k) and 
					dfs(i + k, j, length - k)
				):
					return True

			return False

		return dfs(0, 0, len(s1))
		


# DP
# dp[i][j][len] represents if the s1[i:i+len] and s2[j:j+len] is mutual scrambled
# Note that zero len is meaningless, so the range of len is larger than the range of i or j plus one
class Solution:
	def isScramble(self, s1: str, s2: str) -> bool:
		m, n = len(s1), len(s2)

		dp = [[[False] * (m + 1) for _ in range(m)] for _ in range(m)]

		# When len is 1, it is base case
		for i in range(m):
			for j in range(m):
				if s1[i] == s2[j]:
					dp[i][j][1] = True


		for length in range(2, m + 1):
			for i in range(m - length + 1):  #  preserve the last len positions
				for j in range(m - length + 1):
					for k in range(1, length):
						# First case
						if dp[i][j][k] and dp[i+k][j+k][length-k]:
							dp[i][j][length] = True
							break

						if dp[i][j+length-k][k] and dp[i+k][j][length-k]:
							dp[i][j][length] = True
							break

		return dp[0][0][m]

