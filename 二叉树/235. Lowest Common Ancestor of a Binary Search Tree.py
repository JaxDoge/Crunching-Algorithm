235. Lowest Common Ancestor of a Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
    	candidate = root

        while candidate:
	    	if candidate.val < min(p.val,q.val):
	    		candidate = candidate.right
	    	elif candidate.val > max(p.val,q.val):
	    		candidate = candidate.left 
            else:
            	return candidate