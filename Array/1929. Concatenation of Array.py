1929. Concatenation of Array


class Solution:
	def getConcatenation(self, nums: List[int]) -> List[int]:
		nums.extend(nums)
		return nums