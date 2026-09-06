40. Combination Sum II


class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		n = len(candidates)
		if n == 0:
			return []

		candidates.sort()
		path = []
		ans = []

		self.dfs(candidates, 0, n, path, ans, target)

		return ans


	def dfs(self, cands, start, end, cur_path, res, target):
		# base case
		if target == 0:
			res.append(cur_path.copy())

		for idx in range(start, end):
			if target - cands[idx] < 0:
				break
			if idx > start and cands[idx - 1] == cands[idx]:
				continue

			cur_path.append(cands[idx])
			self.dfs(cands, idx+1, end, cur_path, res, target - cands[idx])
			cur_path.pop()


class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

		candidates.sort()
		n = len(candidates)
		res = []

		def backtrack(idx, cur_path, cur_sum):
			if cur_sum == target:
				res.append(cur_path[:])
			
			if cur_sum > target:
				return
			
			remaining = target - cur_sum
			end = bisect.bisect(candidates, remaining)

			i = idx
			while i < end:
				num = candidates[i]
				cur_sum += num
				cur_path.append(num)
				backtrack(i + 1, cur_path, cur_sum)
				cur_path.pop()
				cur_sum -= num
				while i < end - 1 and candidates[i] == candidates[i + 1]:
					i += 1
				i += 1

			return

		backtrack(0, [], 0)
		return res       