44. Wildcard Matching

# Greedy two-pointer approach
# The core idea is: if we find a mismatch (include pattern depleted faster), we can let the nearest '*' match one more character then try again
# If there is a nearest '*'
# Worst case can still be O(MN)
class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		i = 0
		j = 0

		star = -1 # position of the nearest '*' in p
		match = 0 # if we want to use the nearest '*' (expand it covering range), s[match] will be matched

		while i < len(s):
			# Happy path
			if j < len(p) and (p[j] == s[i] or p[j] == '?'):
				i += 1
				j += 1

			# we find a '*', it is the nearest one so far
			elif j < len(p) and p[j] == '*':
				star = j
				match = i
				# First, let '*' match nothing
				j += 1

			# Sad path, no match or j is out of range
			# If there is the nearest '*'
			elif star != -1:
				match += 1
				# rewind i
				i = match
				# rewind j
				j = star + 1

			else:
				return False

		# Remaining pattern must contain only '*'
		while j < len(p) and p[j] == '*':
			j += 1

		return j == len(p)

# TLE
class Solution:
	def __init__(self):
		self.MEMO = {}
	
	def isMatch(self, s: str, p: str) -> bool:
		if s == '' and p == '':
			return True
		elif s == '':
			# Check the characters in p
			for c in p:
				if c != '*':
					return False
			return True

		elif p == '':
			return False

		return self.dfs(s, 0, p, 0)

	def dfs(self, s, i, p, j):
		# base case
		if j == len(p):
			return i == len(s)

		if i == len(s):
			# check if the rest of characters in p are all *
			for c in p[j:]:
				if c != '*':
					return False
			return True

		# Check memo
		key = (i,j)
		if key in self.MEMO:
			return self.MEMO[key]

		# Carefully list all possible situation
		# 1. i match j, check next position
		if s[i] == p[j] or p[j] in {'?'}:
			res = self.dfs(s, i+1, p, j+1)
		# 2 j is *
		elif p[j] == '*':
			# 2.1 move i
			# 2.2 move j
			res = self.dfs(s, i+1, p, j) or self.dfs(s, i, p, j+1)
		else:
			res = False

		# record result in memo
		self.MEMO[key] = res

		return res


