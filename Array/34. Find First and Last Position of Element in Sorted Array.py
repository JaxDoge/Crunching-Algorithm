34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    	if not nums: return [-1,-1]
    	length = len(nums)
    	
    	def findLeft(left, right):
    		nonlocal nums, target
    		while left <= right:
    			mid = left+(right-left)//2
    			if nums[mid] == target:
    				right = mid-1
    			elif nums[mid] > target:
    				right = mid-1
    			elif nums[mid] < target:
    				left = mid+1
    		if left >= len(nums) or nums[left] != target:
    			return -1
    		return left

    	def findRight(left, right):
    		nonlocal nums, target
    		while left <= right:
    			mid = left+(right-left)//2
    			if nums[mid] == target:
    				left = mid+1
    			elif nums[mid] > target:
    				right = mid-1
    			elif nums[mid] < target:
    				left = mid+1
    		if right < 0 or nums[right] != target:
    			return -1
    		return right

    	left_bound = findLeft(0,length-1)
    	if left_bound == -1:
    		return [-1,-1]
    	else:
    		right_bound = findRight(0,length-1)
    		return [left_bound, right_bound]