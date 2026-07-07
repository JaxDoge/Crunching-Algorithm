1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit


class Solution:
	def longestSubarray(self, nums: List[int], limit: int) -> int:
		max_deque = deque()
		min_deque = deque()
		left = 0
		res = 0

		n = len(nums)

		for right in range(n):
			while max_deque and max_deque[-1] < nums[right]:
				max_deque.pop()
			max_deque.append(nums[right])

			while min_deque and min_deque[-1] > nums[right]:
				min_deque.pop()
			min_deque.append(nums[right])

			while max_deque and min_deque and max_deque[0] - min_deque[0] > limit:
				if max_deque[0] == nums[left]:
					max_deque.popleft()

				if min_deque[0] == nums[left]:
					min_deque.popleft()

				left += 1

			res = max(res, right - left + 1)

		return res
