3737. Count Subarrays With Majority Element I


class Solution:
	def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
		n = len(nums)
		res = 0

		for width in range(1, n + 1):
			counter = 0
			start = 0
			for i in range(width):
				if nums[i] == target:
					counter += 1
			end = start + width - 1

			while end < n:
				if counter > width // 2:
					res += 1

				if nums[start] == target:
					counter -= 1
				start += 1

				end += 1
				if end < n and nums[end] == target:
					counter += 1

		return res


# target -> +1
# others -> -1
class Solution:
	def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
		n = len(nums)

		# Prefix sum is in [-n, n].
		# Shift by n so it can be used as an array index.
		offset = n

		# freq[s + offset] =
		# number of previous prefixes whose transformed prefix sum is s
		freq = [0] * (2 * n + 1)

		# Empty prefix has sum 0
		freq[offset] = 1

		prefix = 0

		# Number of previous prefix sums strictly smaller than `prefix`
		smaller_count = 0

		ans = 0

		for x in nums:
			if x == target:
				# prefix: s -> s + 1
				#
				# Prefixes equal to s now become strictly smaller
				# than the new prefix s + 1.
				smaller_count += freq[prefix + offset]
				prefix += 1

			else:
				# prefix: s -> s - 1
				prefix -= 1

				# Prefixes equal to the new prefix s - 1 used to be
				# smaller than the old prefix s, but are no longer
				# strictly smaller than the new prefix.
				smaller_count -= freq[prefix + offset]

			# Record current prefix for future subarrays
			freq[prefix + offset] += 1

			# Each previous prefix smaller than current prefix gives
			# one positive-sum subarray ending here.
			ans += smaller_count

		return ans
		