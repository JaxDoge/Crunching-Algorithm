27. Remove Element

# 依然是双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    	if not nums: return 0
    	length = len(nums)
    	left = right = 0
    	while right < length:
    		if nums[right] != val:
    			# 主要思想是把 later part 中非 val 元素交换到前面来，考虑到题目条件，也可以不交换直接赋值
    			# left 标记如果后面有需要交换的元素，因该放到哪里
    			nums[left] = nums[right]
    			left += 1
    		right += 1
    	return left
