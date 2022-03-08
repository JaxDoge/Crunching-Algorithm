560. Subarray Sum Equals K


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    	n = len(nums)

    	# Use a hashmap to record the appearances of a presum
    	presum_dict = dict()

    	# base case
    	res = 0
    	sum_0_i = 0
    	presum_dict.update({0:1})


    	for i in range(n):
    		sum_0_i += nums[i]
    		# the presum that could meet the requirement
    		sum_0_j = sum_0_i - k
    		# if we recorded the presum previously, add the count to the res
    		if sum_0_j in presum_dict:
    			res += presum_dict[sum_0_j]
    		# update the presum dictionary
    		presum_dict.update({sum_0_i:presum_dict.get(sum_0_i,0)})

    	return res
