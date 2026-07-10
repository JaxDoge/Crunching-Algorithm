1022. Sum of Root To Leaf Binary Numbers



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
		binary_list = []
		res_list = []

		def preorder(node: TreeNode):
			nonlocal binary_list, res_list

			binary_list.append(str(node.val))

			if not node.left and not node.right:
				res_list.append(int(''.join(binary_list), 2))
				binary_list.pop()
				return

			if node.left:
				preorder(node.left)

			if node.right:
				preorder(node.right)

			binary_list.pop()

		preorder(root)

		return sum(res_list)


# We can also track current sum with the node traversal

class Solution:
	def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
		def preorder(node, curr_sum):
			nonlocal root_to_leaf

			if node:
				curr_sum = (curr_sum << 1) | node.val
				if not node.left and not node.right:
					root_to_leaf += curr_sum

				preorder(node.left, curr_sum)
				preorder(node.right, curr_sum)

		root_to_leaf = 0
		preorder(root, 0)

		return root_to_leaf

