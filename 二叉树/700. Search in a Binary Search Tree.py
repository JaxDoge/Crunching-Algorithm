700. Search in a Binary Search Tree

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


# 递归框架
class Solution:
	def searchBST(self, root: TreeNode, val: int) -> TreeNode:
		node = root
		def helper(node, val):
			if not node: return None
		    if val == node.val:
		    	return node 
		    elif val > node.val:
		    	return helper(node.right, val)
		    elif val < node.val:
		    	return helper(node.left, val)
		return helper(root, val)


# 迭代方法，常量额外空间

class Solution:
	def searchBST(self, root: TreeNode, val: int) -> TreeNode:
		while root and val != root.val:
			if val > root.val:
				root = root.right
			elif val < root.val:
				root = root.left
		return root

