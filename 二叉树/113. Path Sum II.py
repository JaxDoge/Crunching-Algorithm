113. Path Sum II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
	def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
		if not root:
			return []

		res = []

		def preorderTraver(node, target, path):
			if not node: return
			path.append(node.val)
			target = target - node.val
			if target == 0 and not node.left and not node.right:
				res.append(path[:])
			preorderTraver(node.left, target, path)
			preorderTraver(node.right, target, path)
			path.pop()
			return
		preorderTraver(root, targetSum, [])    
		return res  
