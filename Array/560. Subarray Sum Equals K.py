560. Subarray Sum Equals K


# Note the left presum array has presum[j] - presum[i] = sum(nums[i+1...j]), i<j
# So if we know the rest = presum[j] - k has appeared before (along with the appearance), we can update the result
# Need a hashmap to count all previous presum appearance
# Update the hashmap counter on the fly


class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		n = len(nums)

		# Empty subarray only appear once, to match nums[i] == k
		presum_hashmap = dict({0:1})

		res = 0

		presum = 0

		for i in range(n):
			presum += nums[i]
			rest = presum - k
			if rest in presum_hashmap:
				res += presum_hashmap[rest]

			# update the hashmap, appearance + 1
			presum_hashmap.update({presum:presum_hashmap.get(presum, 0) + 1})

		return res
