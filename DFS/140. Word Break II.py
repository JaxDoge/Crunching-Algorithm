140. Word Break II


# DFS + MEMO
# OR DP table 
from collections import defaultdict
class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
		n = len(s)
		m = len(wordDict)
		wordMap = defaultdict(list)

		for i in range(m):
			fL = wordDict[i][0]
			wordMap[fL].append(wordDict[i])

		memo = {}
		# backtrack will find all valid path for s[start:]
		# return list[list]
		def backtrack(start):
			nonlocal memo, m, n, s, wordMap
			# base case
			if start == n:
				return [[]]

			if start in memo:    
				return memo[start]


			firstL = s[start]
			curPaths = []
			for w in wordMap[firstL]:
				span = len(w)
				targetW = s[start:start+span]
				if w == targetW:
					# choose w, get the result of s[start+len(w):]
					restPaths = backtrack(start+span)
					for rp in restPaths:
						curPaths.append([w]+rp[:])

			memo[start] = curPaths

			return curPaths
		res = backtrack(0)
		return ["".join(x) for x in res]


# DP solution
class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
		words_map = set(wordDict)
		n = len(s)

		# dp[i] = all sentences that can construct s[:i]
		dp = [[] for _ in range(n + 1)]
		dp[0] = [""]
		
		for i in range(1, n + 1):
			for j in range(i):
				word = s[j:i]

				if word not in words_map:
					continue
				
				for sentence in dp[j]:
					if sentence:
						dp[i].append(sentence + ' ' + word)
					else:
						dp[i].append(word)
		
		return dp[-1]