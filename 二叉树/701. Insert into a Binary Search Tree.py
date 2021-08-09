701. Insert into a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    	o_root = root

    	if not root:
    		root = TreeNode(val = val)
    	while root:
    		if val >= root.val:
    			if root.right:
    			    root = root.right
    			else:
    				root.right = TreeNode(val = val)
    				break
    		elif val <= root.val:
    			if root.left:
    			    root = root.left
    			else:
    				root.left = TreeNode(val = val)
    				break
    	return o_root
