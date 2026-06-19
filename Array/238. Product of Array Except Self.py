238. Product of Array Except Self


# The answer of position i is the product of all numbers' production to the left and to the right.
# So we can have two new array, in the left_prod[i], we have the production of nums[0] ... num[i-1]
# and similar to the right_prod[i].
# We can construct these two array in O(n) because the production contain all previous information.
# left_prod[i] * right_prod[i] is answer[i]



class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		left_prod = [0] * n
		right_prod = [0] * n
		answer = [0] * n

		# construct left_prod
		left_prod[0] = 1
		for i in range(1, n):
			j = i - 1
			left_prod[i] = left_prod[j] * nums[j]

		# construct right_prod
		right_prod[n - 1] = 1
		for i in range(n - 2, -1, -1):
			j = i + 1
			right_prod[i] = right_prod[j] * nums[j]

		for i in range(n):
			answer[i] = left_prod[i] * right_prod[i]

		return answer




# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Using answer list as the left_prod and calculate right_prod on the fly

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		answer = [0] * n

		answer[0] = 1
		for i in range(1, n):
			j = i - 1
			answer[i] = answer[j] * nums[j]

		right_prod = 1
		for i in range(n - 1, -1, -1):
			if i < n - 1:
				right_prod = right_prod * nums[i + 1]			
			answer[i] = answer[i] * right_prod

		return answer

