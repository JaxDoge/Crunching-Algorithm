987. Vertical Order Traversal of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
		# Root must be existed

		colTable = defaultdict(list)
		bounds = [0, 0]

		def preorder(node, row, col):
			if not node:
				return

			colTable[col].append((row, node.val))
			bounds[0] = min(bounds[0], col)
			bounds[1] = max(bounds[1], col)

			preorder(node.left, row + 1, col - 1)
			preorder(node.right, row + 1, col + 1)

		preorder(root, 0, 0)

		res = []

		for col in range(bounds[0], bounds[1] + 1):
			res.append([val for row, val in sorted(colTable[col])])

		return res