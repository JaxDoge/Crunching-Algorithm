366. Find Leaves of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We need to use post order traverse because the parent need the height info from both children
# Shared height means same level
# If current height never exists in the solution before, append a new list

class Solution:
	def __init__(self):
		self.solution = []

	def _postorder(self, node):
		# Base case
		if not node:
			return -1

		left_h = self._postorder(node.left)
		right_h = self._postorder(node.right)

		cur_height = max(left_h, right_h) + 1

		# Add current node to the solution
		# Check if the height has been recorded
		if cur_height == len(self.solution):
			self.solution.append([])

		self.solution[cur_height].append(node.val)

		return cur_height

	def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
		self._postorder(root)
		return self.solution