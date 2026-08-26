14. Longest Common Prefix


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		n = len(strs)

		i = 0
		j = 0
		checker = list()
		ans = list()
		while True:
			# Base case, if any string is empty or the shortest string is shorter than index j, just break the loop 
			if strs[i] == "" or j >= len(strs[i]):
				break

			# if current string is the first one or current index character equal to the previous character in different string, continue
			# Otherwise just break
			if i == 0 or strs[i][j] == checker[0]:
				checker.append(strs[i][j])
				i += 1
			else:
				break

			# All strings are checked on the j index, ready for the next loop
			if len(checker) == n:
				ans.append(checker[0])
				i = 0
				j += 1
				checker = list()

		return ''.join(ans)


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		res = list(strs[0])
		for s in strs:
			cur_cmn_pre = []
			i = 0
			n = len(res)
			for c in s:
				if i >= n:
					break
				if c == res[i]:
					cur_cmn_pre.append(c)
					i += 1
				else:
					break

			if len(cur_cmn_pre) == 0:
				return ""
			res = cur_cmn_pre
		
		return "".join(res)

