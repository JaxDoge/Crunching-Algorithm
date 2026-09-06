47. Permutations II

class Solution:
	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		n = len(nums)
		res = []

		def backtrack(first):
			if first == n:
				res.append(nums.copy())
				return

			seen = set()

			for i in range(first, n):
				if nums[i] in seen:
					continue
					
				seen.add(nums[i])
				nums[first], nums[i] = nums[i], nums[first]
				backtrack(first + 1)
				nums[first], nums[i] = nums[i], nums[first]


		backtrack(0)

		return res

