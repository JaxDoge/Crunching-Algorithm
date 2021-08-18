110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
    	def treeHeight(node):
    		if not node: return 0
    		left_height = treeHeight(node.left)
    		right_height = treeHeight(node.right)
    		if left_height == -1 or right_height == -1:
    			return -1
    		if abs(left_height - right_height) > 1:
    			return -1
            
    		return max(left_height+1, right_height+1)
        
        res = treeHeight(root)
    	return if not res == -1