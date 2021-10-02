496. Next Greater Element I

# Monotonous stack
# hashmap
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	len_1 = len(nums1)
    	len_2 = len(nums2)

    	# the hashmap of nums2, value is the next greater element of nums2[i]
    	next_greater_dict = dict()
    	help_stack = []
    	for i in range(len_2-1,-1,-1):
    		while help_stack and nums2[i] >= help_stack[len(help_stack)-1]:
    			help_stack.pop()
    		if not help_stack:
    			next_greater_dict[nums2[i]] = -1
    		else:
    			next_greater_dict[nums2[i]] = help_stack[len(help_stack)-1]
    		help_stack.append(nums2[i])

    	ans = []
    	for i in range(len_1):
    		num = nums1[i]
    		ans.append(next_greater_dict[num])
    	return ans