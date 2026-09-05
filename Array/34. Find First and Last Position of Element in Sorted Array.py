34. Find First and Last Position of Element in Sorted Array

class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:
		n = len(nums)
		if not n:
			return [-1, -1]

		def lower_bound(x):
			left, right = 0, n - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] >= x:
					right = mid - 1
				elif nums[mid] < x:
					left = mid + 1

			return left

		start = lower_bound(target)
		if start == n or nums[start] != target:
			return [-1, -1]
		
		end = lower_bound(target + 1)
		return [start, end - 1]