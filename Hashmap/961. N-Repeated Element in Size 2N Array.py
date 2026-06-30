961. N-Repeated Element in Size 2N Array

class Solution:
	def repeatedNTimes(self, nums: List[int]) -> int:
		n = len(nums)
		set_counter = set()

		for i in range(n):
			num = nums[i]
			if num in set_counter:
				return num
			set_counter.add(num)