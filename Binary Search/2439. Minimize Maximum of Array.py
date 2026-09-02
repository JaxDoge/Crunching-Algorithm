2439. Minimize Maximum of Array


# Binary search
# From right to left. Unload the value to the left neighbor
class Solution:
	def minimizeArrayValue(self, nums: List[int]) -> int:
		n = len(nums)
		low = nums[0]
		high = max(nums)

		def check(threshold):
			tmp_nums = nums[:]

			for i in range(n - 1, 0, -1):
				if tmp_nums[i] <= threshold:
					continue
				carry = tmp_nums[i] - threshold
				tmp_nums[i - 1] += carry

			if tmp_nums[0] > threshold:
				return False

			return True

		while low <= high:
			mid = (low + high) // 2
			if check(mid):
				high = mid - 1
			else:
				low = mid + 1

		return low






