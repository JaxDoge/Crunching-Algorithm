1679. Max Number of K-Sum Pairs


class Solution:
	def maxOperations(self, nums: List[int], k: int) -> int:
		n = len(nums)
		counter = 0
		hashmap = {}

		# Build the dictionary to quick query rest of each number and match target [rest, target] 
		for i in range(n):
			hashmap.setdefault(nums[i], [0, k - nums[i]])[0] += 1

		for cur_num, value in hashmap.items():
			# iterate all rest of current number
			while value[0] > 0:
				# subtract current number rest
				# Mush put this line before the target judgement.
				# In case the target value is the same as current value
				value[0] -= 1
				
				# no more target, break early
				if value[1] not in hashmap or hashmap[value[1]][0] < 1:
					break

				# subtract target number rest
				hashmap[value[1]][0] -= 1

				counter += 1

		return counter

