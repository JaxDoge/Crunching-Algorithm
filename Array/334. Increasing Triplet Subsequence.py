334. Increasing Triplet Subsequence


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
    	n = len(nums)
    	first = second = float("inf")

    	for i in range(n):
    		cur = nums[i]
    		if cur <= first:
    			first = cur
    		elif cur <= second:
    			second = cur
    		else:
    			return True

    	return False



# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?