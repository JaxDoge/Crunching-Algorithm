28. Implement strStr()


# GO GO GO KMP
class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if not needle:
			return 0
		n = len(haystack)
		m = len(needle)

		dp = [[0]*256 for _ in range(m)]
		dp[0][ord(needle[0])] = 1

		X = 0
		# Note that j start from index 1
		for j in range(1, m):
			for c in range(0, 256):
				dp[j][c] = dp[X][c]
			dp[j][ord(needle[j])] = j + 1
			X = dp[X][ord(needle[j])]

		J = 0
		for i in range(n):
			J = dp[J][ord(haystack[i])]
			if J == m:
				return i - m + 1
		return -1


class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		m = len(haystack)
		n = len(needle)

		if n > m:
			return -1

		return haystack.find(needle)


# Standard KMP
class Solution:
	def buildLPS(self, pattern):
		m = len(pattern)
		length = 0
		i = 1
		lps = [0] * m

		while i < m:
			# Check if we can extend the lps in substring [...i]
			if pattern[i] == pattern[length]:
				length += 1
				lps[i] = length
				i += 1
			else:
				# Don't fall all the way back to the beginning of pattern
				# Fallback and reuse previous match length
				if length != 0:
					length = lps[length - 1]
				else:
					lps[i] = 0
					i += 1

		return lps

	def strStr(self, haystack: str, needle: str) -> int:
		n = len(haystack)
		m = len(needle)
		if n < m:
			return -1

		lps = self.buildLPS(needle)

		i = 0
		j = 0

		while i < n:
			if haystack[i] == needle[j]:
				i += 1
				j += 1

				if j == m:
					# j = lps[j - 1]
					return i - m

			else:
				if j != 0:
					j = lps[j - 1]

				else:
					i += 1

		return -1
























