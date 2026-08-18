3660. Jump Game IX

# Note that if i can jump to j, then j can jump back to i
# [ ... left ... ] | [ ... right ... ] if the left max <= right min. They are splited groups

class Solution:
	def maxValue(self, nums: List[int]) -> List[int]:
		n = len(nums)
		suffix_min = [0] * n
		suffix_min[-1] = nums[-1]

		for i in range(n - 2, -1, -1):
			suffix_min[i] = min(suffix_min[i + 1], nums[i])

		ans = [0] * n

		# we need a start point for current group, so we know which segment to update the ans list
		# The start point will move to the next split point
		start = 0
		cur_max = nums[0]

		for i in range(n):
			cur_max = max(cur_max, nums[i])

			# we find a split point
			if i == n - 1 or cur_max <= suffix_min[i + 1]:
				# update ans segment
				for j in range(start, i + 1):
					ans[j] = cur_max

				start = i + 1
				if start < n:
					cur_max = nums[start]

		return ans


