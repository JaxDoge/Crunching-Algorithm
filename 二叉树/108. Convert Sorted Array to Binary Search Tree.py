108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
		def range_to_tree(low, high):
			if low > high:
				return None
			
			mid = (low + high) // 2
			root = TreeNode(nums[mid])

			root.left = range_to_tree(low, mid-1)
			root.right = range_to_tree(mid+1, high)

			return root
		
		return range_to_tree(0, len(nums)-1)


