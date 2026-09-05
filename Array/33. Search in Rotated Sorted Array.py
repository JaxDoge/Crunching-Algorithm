33. Search in Rotated Sorted Array


# Bisect
# Divide the array into two parts, and one of them must be ordered
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		if not nums:
			return -1

		n = len(nums)
		l = 0
		r = n - 1

		while l <= r:
			mid = l + (r - l) // 2

			if nums[mid] == target:
				return mid

			# figure out which part is ordered
			# Consider boundary case [3,1], target is 1, which the l == mid at first iter. There must be only two element left to check, we hope move l to l + 1
			elif nums[0] <= nums[mid]:
				# previous part is ordered
				if nums[0] <= target < nums[mid]:
					r = mid - 1
				else:
					l = mid + 1
			else:
				# later part is ordered
				if nums[mid] < target <= nums[n-1]:
					l = mid + 1
				else:
					r = mid - 1

		return -1

# Like this one
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		n = len(nums)
		low, high = 0, n - 1
		while low <= high:
			mid = (low + high) // 2

			if nums[mid] == target:
				return mid

			elif nums[mid] >= nums[low]:
				if nums[low] <= target < nums[mid]:
					high = mid - 1
				else:
					low = mid + 1

			else:
				if nums[mid] < target <= nums[high]:
					low = mid + 1
				else:
					high = mid - 1
			
		return -1