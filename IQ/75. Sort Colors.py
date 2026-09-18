75. Sort Colors


# Double pointers
# I'll call it triple pointers
# Detail-Oriented!
class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		p0 = 0 # the next position of next zero
		p2 = n - 1 # the next position of next two

		for i in range(n):
			if i > p2:
				break

			while i <= p2 and nums[i] == 2:
				# continuously change change the value at i and p2, until there is no two at the left of i
				nums[i], nums[p2] = nums[p2], nums[i]
				p2 -= 1

			if nums[i] == 0:
				# change the value at i and p0
				# p0 will always point to the true next zero position or equals to i
				nums[i], nums[p0] = nums[p0], nums[i]
				p0 += 1

		return


| Region               | Contents          |
| -------------------- | ----------------- |
| `nums[:low]`         | All `0`s          |
| `nums[low:mid]`      | All `1`s          |
| `nums[mid:high + 1]` | Not yet inspected |
| `nums[high + 1:]`    | All `2`s          |


class Solution:
	def sortColors(self, nums: list[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		# low: where the next 0 belongs.
		# mid: the current element to inspect.
		# high: where the next 2 belongs.

		n = len(nums)
		low = mid = 0
		high = n - 1

		while mid <= high:
			if nums[mid] == 0:
				nums[low], nums[mid] = nums[mid], nums[low]
				low += 1
				mid += 1
			elif nums[mid] == 1:
				mid += 1
			elif nums[mid] == 2:
				nums[high], nums[mid] = nums[mid], nums[high]
				high -= 1