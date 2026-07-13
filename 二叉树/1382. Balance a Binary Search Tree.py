1382. Balance a Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def _inorder(self, node, arr):
		if not node:
			return

		self._inorder(node.left, arr)
		arr.append(node.val)
		self._inorder(node.right, arr)


	def _construct(self, arr, start, end):
		if start > end:
			return None

		mid = (start + end) >> 1

		left = self._construct(arr, start, mid-1)
		right = self._construct(arr, mid+1, end)

		node = TreeNode(arr[mid], left, right)
		return node


	def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		inorder = []

		self._inorder(root, inorder)

		return self._construct(inorder, 0, len(inorder)-1)