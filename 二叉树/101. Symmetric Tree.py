101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归解法

class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		def symmetricCheck(p: TreeNode, q: TreeNode) -> bool:
			if not p and not q:
				return True

			if not p or not q:
				return False

			if p.val != q.val:
				return False
			
			return symmetricCheck(p.left, q.right) and symmetricCheck(p.right, q.left)
		return symmetricCheck(root, root)



class Solution:
	def isSymmetric(self, root: TreeNode | None) -> bool:
		left_stack = [root.left]
		right_stack = [root.right]

		while left_stack and right_stack:
			left_pop = left_stack.pop()
			right_pop = right_stack.pop()

			if not (left_pop and right_pop):
				if left_pop != right_pop:
					return False
				continue
			
			if left_pop.val != right_pop.val:
				return False
			
			left_stack.extend([left_pop.right, left_pop.left])
			right_stack.extend([right_pop.left, right_pop.right])

		return True