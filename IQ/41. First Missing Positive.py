41. First Missing Positive

# Note that for an array of length n, the answer must be in [1, n + 1].
# So we only care about values 1...n. Ideally, we want: 
# idx 0 -> 1
# idx 1 -> 2
# idx n-1 -> n
# This is essentially using the input array itself as a hash table: index i represents whether number i + 1 exists.

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		n = len(nums)

		for i in range(n):
			while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
				j = nums[i] - 1
				nums[i], nums[j] = nums[j], nums[i]

		for i in range(n):
			if nums[i] != i + 1:
				return i + 1

		return n + 1