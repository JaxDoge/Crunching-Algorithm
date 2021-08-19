112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

    	def preorderTraver(node, target):
	    	if not node: return False
    		target = target - node.val
    		if target == 0 and not node.left and not node.right:
    			return True
            return preorderTraver(node.left, target) or preorderTraver(node.right, target)
        return preorderTraver(root, targetSum)