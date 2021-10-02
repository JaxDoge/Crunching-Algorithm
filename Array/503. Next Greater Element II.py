503. Next Greater Element II

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
    	length = len(nums)
    	# Find out the largest number in the list
    	largest: int = nums[0]
    	largest_index: int = 0
    	for i in range(1,length):
    		if nums[i] > largest:
    			largest_index = i
    			largest = nums[i]


    	res: List[int] = [-1] * length
    	help_stack: List[int] = []
    	real_index: int = largest_index
    	for _ in range(length):
    		while help_stack and help_stack[len(help_stack)-1] <= nums[real_index]:
    			help_stack.pop()
    		if help_stack:
    			res[real_index] = help_stack[len(help_stack)-1]
    		help_stack.append(nums[real_index])
    		if real_index == 0:
    			real_index = length - 1
    		else:
    			real_index -= 1

    	return res
    			

# 顺序压栈
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stk = list()

        # 利用取模实现循环
        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)
        
        return ret
