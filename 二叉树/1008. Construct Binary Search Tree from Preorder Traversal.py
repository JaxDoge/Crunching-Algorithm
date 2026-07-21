1008. Construct Binary Search Tree from Preorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Construct the tree in preorder

class Solution:
	def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
		n = len(preorder)
		cur_idx = 0

		def buildTree(low, high):
			nonlocal cur_idx
			if cur_idx >= n:
				return None

			cur_val = preorder[cur_idx]

			# Judge if current value can be placed in this subtree
			if cur_val < low or cur_val > high:
				return None

			cur_node = TreeNode(val = cur_val)

			cur_idx += 1
			# left subtree cannot larger than cur_val
			cur_node.left = buildTree(low, cur_val)
			# right subtree cannot smaller than cur_val
			cur_node.right = buildTree(cur_val, high)

			return cur_node


		return buildTree(float('-inf'), float('inf'))