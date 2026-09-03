18. 4Sum


class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		n = len(nums)
		if n < 4:
			return []

		res = []
		nums.sort()

		for i in range(n-3):
			if i > 0 and nums[i] == nums[i - 1]:
				continue

			for j in range(i+1, n-2):
				if j > i + 1 and nums[j] == nums[j - 1]:
					continue

				L = j + 1
				R = n - 1

				while L < R:
					quad_sum = nums[i] + nums[j] + nums[L] + nums[R]

					# move the two pointers in different scenarios
					if quad_sum == target:
						res.append([nums[i], nums[j], nums[L], nums[R]])
						# find the next one;
						while L < R and nums[L] == nums[L + 1]:
							L += 1
						while L < R and nums[R] == nums[R - 1]:
							R -= 1

						L += 1
						R -= 1

					elif quad_sum < target:
						L += 1
					elif quad_sum > target:
						R -= 1

		return res

# Generic solution
class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

		def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
			res = []

			# If we have run out of numbers to add, return res.
			if not nums:
				return res

			# There are k remaining values to add to the sum. The
			# average of these values is at least target // k.
			average_value = target // k

			# We cannot obtain a sum of target if the smallest value
			# in nums is greater than target // k or if the largest
			# value in nums is smaller than target // k.
			if average_value < nums[0] or nums[-1] < average_value:
				return res

			if k == 2:
				return twoSum(nums, target)

			for i in range(len(nums)):
				if i == 0 or nums[i - 1] != nums[i]:
					for subset in kSum(nums[i + 1 :], target - nums[i], k - 1):
						res.append([nums[i]] + subset)

			return res

		def twoSum(nums: List[int], target: int) -> List[List[int]]:
			res = []
			lo, hi = 0, len(nums) - 1

			while lo < hi:
				curr_sum = nums[lo] + nums[hi]
				if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
					lo += 1
				elif curr_sum > target or (
					hi < len(nums) - 1 and nums[hi] == nums[hi + 1]
				):
					hi -= 1
				else:
					res.append([nums[lo], nums[hi]])
					lo += 1
					hi -= 1

			return res

		nums.sort()
		return kSum(nums, target, 4)