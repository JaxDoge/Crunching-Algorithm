104. Maximum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		if not root: 
			return 0
		left_height = self.maxDepth(root.left)
		right_height = self.maxDepth(root.right)
		return max(left_height,right_height) + 1



class Solution:
	def maxDepth(self, root: TreeNode | None) -> int:
		if not root:
			return 0

		queue = deque()
		queue.append(root)
		res = 0

		while queue:
			cur_level_size = len(queue)

			for i in range(cur_level_size):
				node = queue.popleft()
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
			res += 1

		return res