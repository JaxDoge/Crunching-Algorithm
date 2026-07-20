968. Binary Tree Cameras


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We start from the leaves and trace back to the root
# We shouldn't put cameras in leaves
# The most effecient way is put cameras in a node where at least one child is not covered
# or there is NO parent to cover this uncovered node.

class Solution:
	def minCameraCover(self, root: Optional[TreeNode]) -> int:
		res = 0

		# Important! If a child is missing, we don't need to cover it
		# So treat None child as covered.
		covered = {None}

		def postorder(node, parent):
			nonlocal res
			if not node:
				return

			postorder(node.left, node)
			postorder(node.right, node)

			if (parent is None and node not in covered) or (node.left not in covered) or (node.right not in covered):
				res += 1
				covered.update({node, parent, node.left, node.right})

		postorder(root, None)
		return res