81. Search in Rotated Sorted Array II


#  bisection
class Solution:
	def search(self, nums: List[int], target: int) -> bool:

		l, r = 0, len(nums) - 1

		while l <= r:
			mid = l + (r - l) // 2

			if nums[mid] == target:
				return True

			# Because of duplication, we may not decide with part is sorted by comparing nums[mid] with two ends
			if nums[mid] == nums[l] and nums[mid] == nums[r]:
				l += 1
				r -= 1
				continue

			if nums[l] <= nums[mid]:
				if nums[l] <= target < nums[mid]:
					r = mid - 1
				else:
					l = mid + 1

			else:
				if nums[mid] < target <= nums[r]:
					l = mid + 1
				else:
					r = mid - 1


		return False

# Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
Yes. Duplicates change the worst-case time complexity from O(log n) to O(n).