410. Split Array Largest Sum

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
    	# reverse thinking, calculate the minimal sub-array nums for a given max sub-array sum
    	def split(max_sub: int) -> int:
    		nonlocal nums
    		split = 0
    		sub_sum = 0
    		for ele in nums:
    			if sub_sum+ele > max_sub:
    				split += 1
    				sub_sum = ele
    			else:
    				sub_sum += ele
    		return split + 1

		# the upperbound and lowerbound of max_sub
		lower = max(nums)
		upper = sum(nums)

		while lower<=upper:
			mid = lower + (upper-lower)//2
			if split(mid) <= m:
				upper = mid - 1
			elif split(mid) > m:
				lower = mid + 1

		return lower


