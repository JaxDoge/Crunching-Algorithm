89. Gray Code


# Backtrak
class Solution:
	def grayCode(self, n: int) -> list[int]:
		seq_len = 2 ** n
		seen = set()
		res = []
		def dfs(path, cur_num):
			# Successfully find a sequence
			if len(path) == seq_len:
				if cur_num == 0:
					res.extend(path)
				return
			
			# cur_num already in path
			if cur_num in seen:
				return
			
			# Add cur_num in path
			seen.add(cur_num)
			path.append(cur_num)

			# Change one bit
			for i in range(n):
				mask = 1 << i
				cand = cur_num ^ mask
				dfs(path, cand)
				if res: break

			path.pop()
			seen.remove(cur_num)

		dfs([], 0)
		return res



# Formula
# https://baike.baidu.com/item/%E6%A0%BC%E9%9B%B7%E7%A0%81
class Solution:
	def grayCode(self, n: int) -> List[int]:
		ans = [0] * (1 << n)
		for i in range(1 << n):
			ans[i] = (i >> 1) ^ i
		return ans


class Solution:
	def grayCode(self, n: int) -> list[int]:
		res = [0]

		for i in range(n):
			mask = 1 << i
			for j in range(len(res) - 1, -1, -1):
				res.append(res[j] | mask)

		return res