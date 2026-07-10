545. Boundary of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# preorder. Since we need the parent info to decide if child belongs to the boundary
# 1 is in left boundary, 2 for right and 3 is others (middle nodes)

class Solution:
	def _isLeaf(self, node):
		return not node.left and not node.right

	def _isLeftBoundary(self, flag):
		return flag == 1

	def _isRightBoundary(self, flag):
		return flag == 2

	def _isRoot(self, flag):
		return flag == 0

	def _leftChildFlag(self, cur_node, cur_flag):
		if self._isLeftBoundary(cur_flag) || self._isRoot(cur_flag):
			return 1
		elif self._isRightBoundary(cur_flag) and not cur_node.right:
			return 2
		else:
			return 3

	def _rightChildFlag(self, cur_node, cur_flag):
		if self._rightBoundary(cur_flag) || self._isRoot(cur_flag):
			return 2
		elif self._isLeftBoundary(cur_flag) and not cur_node.left:
			return 1
		else:
			return 3

	def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
		res = [root.val]
		left_bound = []
		leaf_bound = []
		right_bound = deque()

		def preorder(node, flag):
			nonlocal left_bound, leaf_bound, right_bound

			if not node:
				return

			if self._isLeftBoundary(flag):
				left_bound.append(node.val)
			elif self._isRightBoundary(flag):
				right_bound.appendleft(node.val)
			elif self._isLeaf(node) and not self._isRoot(flag):
				leaf_bound.append(node.val)

			preorder(node.left, self._leftChildFlag(node, flag))
			preorder(node.right, self._rightChildFlag(node, flag))

		preorder(root, 0)

		res.extend(left_bound)
		res.extend(leaf_bound)
		res.extend(right_bound)

		return res
