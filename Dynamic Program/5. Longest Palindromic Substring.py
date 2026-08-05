5. Longest Palindromic Substring

# Dynamic Program
# status transform formula Dij = Di+1j-1 and Di == Dj
# There are two exceptions, i = i and i + 1 = j
# Zigzag Scanning
class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		if n <= 1:
			return s

		ps, pe = 0, 0

		dp = [[False] * n for _ in range(n)]

		for i in range(n):
			dp[i][i] = True
		
		for i in range(n-2, -1, -1):
			for j in range(i + 1, n):
				if s[i] != s[j]:
					continue
				elif j - i == 1:
					dp[i][j] = True
				elif dp[i + 1][j - 1]:
					dp[i][j] = True
				
				# Only update the ps and pe if we find a longest one.
				if dp[i][j] and (j - i + 1) > (pe - ps + 1):
					ps = i
					pe = j
		
		return s[ps:pe + 1]