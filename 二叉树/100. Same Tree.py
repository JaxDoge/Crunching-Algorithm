100. Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 迭代，紫金算法
class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
		p_stack = [p]
		q_stack = [q]

		while p_stack and q_stack:
			p_top = p_stack.pop()
			q_top = q_stack.pop()
			
			# 先处理特殊情况
			if not (p_top and q_top):
				# 两者至少一个为空
				if p_top != q_top:
					# 且不同时为空
					return False
				else:
					# 且同时为空
					continue

			if p_top.val != q_top.val:
				return False

			# 两者均不为空指针
			p_stack.extend([p_top.right,p_top.left])
			q_stack.extend([q_top.right,q_top.left])

		return True



class Solution:
	def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
		if not p and not q:
			return True

		def preorder(root_1, root_2):
			if not root_1 and root_2:
				return False
			elif root_1 and not root_2:
				return False
			elif not root_1 and not root_2:
				return True
			elif root_1.val != root_2.val:
				return False
			
			res = preorder(root_1.left, root_2.left)
			if not res:
				return res
			res = preorder(root_1.right, root_2.right)

			return res
		
		return preorder(p, q)