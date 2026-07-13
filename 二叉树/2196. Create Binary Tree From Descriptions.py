2196. Create Binary Tree From Descriptions


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def __init__(self):
		self.val2node = {}

	def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
		root_cand = set()

		for parent, child, isLeft in descriptions:
			# Check if parent exist before
			if parent in self.val2node:
				parent_node = self.val2node[parent]
			else:
				parent_node = TreeNode(val = parent)
				self.val2node[parent] = parent_node
				root_cand.add(parent_node)

			if child in self.val2node:
				child_node = self.val2node[child]
				root_cand.discard(child_node)
			else:
				child_node = TreeNode(val = child)
				self.val2node[child] = child_node

			if isLeft:
				parent_node.left = child_node
			else:
				parent_node.right = child_node

		return list(root_cand)[0]



