26. Remove Duplicates from Sorted Array

# 超时
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	left = 0
    	length = len(nums)
    	while True:
    		right = left
    		while right < length-1 and nums[right] == nums[right+1]:
    			right += 1
    			if right == length-1: return left + 1
    		if right != left:
    			nums[right], nums[right+1] = nums[right+1], nums[right]
    			continue
    		if left < length-1:
    			left += 1
    		else:
    			return left + 1

# 快慢指针直接赋值不交换
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	if not nums: return 0
    	left = 0
    	right = 0
    	length = len(nums)

    	while right < length:
    		# 快指针探路，发现新数就赋值给 slow ++
    		# 覆盖边际情况，严格递增数列
    		if nums[left] != nums[right]:
    			left += 1
    			nums[left] = nums[right]
    		right += 1
    	return left+1
