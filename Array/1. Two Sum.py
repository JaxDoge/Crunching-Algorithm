1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	nums_dict = dict()
    	for i, num in enumerate(nums):
    		left_num = target-num
    		if left_num in nums_dict:
    			return [nums_dict[left_num], i]
    		nums_dict[nums[i]] = i 


# Another solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = collections.defaultdict(list)
        n = len(nums)

        for i in range(n):
            cur = nums[i]
            for j in vals[target-nums[i]]:
                return [i, j]
            vals[cur].append(i)



# 2022 7 16 review 1