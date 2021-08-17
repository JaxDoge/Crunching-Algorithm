108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 无额外空间开销
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    	# Badcase
		if not nums: return None

        def treeConstructor(nums, low, high):
            if low > high: return None
   
            root_index = int((low+high)/2)
		    root_val = nums[root_index]
			root = TreeNode(val = root_val)

			root.left = treeConstructor(nums, low, root_index-1)
			root.right = treeConstructor(nums, root_index+1, high)
			return root
        res = treeConstructor(nums, 0, len(nums)-1)
        return res


