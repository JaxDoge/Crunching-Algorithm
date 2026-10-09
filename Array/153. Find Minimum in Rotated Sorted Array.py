153. Find Minimum in Rotated Sorted Array




class Solution:
	def findMin(self, nums: List[int]) -> int:
		n = len(nums)

		left, right = 0, n - 1

		while left <= right:
			mid = left + (right - left) // 2
			
			# if the right part is sorted in ascending order, the minimum must be in either left part or the mid itself
			# So we retain the mid point
			if nums[mid] < nums[right] :
				right = mid
			
			# Otherwise minimum won't be in mid (or at least not just in mid), so we don't need to retain mid
			elif nums[mid] >= nums[right]:
				left = mid + 1



		return nums[right]  # return the number at right index, because left = right + 1 = mid + 1 in the end