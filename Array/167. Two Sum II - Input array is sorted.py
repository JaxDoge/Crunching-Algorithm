167. Two Sum II - Input array is sorted

# 有序数组，考虑用二分查找，不断移动左右指针搜索
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    	left = 0
    	right = len(numbers) - 1
    	while left < right:
    		sum_up = numbers[left] + numbers[right]
    		if sum_up == target:
    			return [left+1, right+1]
    		elif sum_up > target:
    			right -= 1
    		elif sum_up < target:
    			left += 1
    	return [-1,-1]