314. Binary Tree Vertical Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
	def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []

		col_hashtable = defaultdict(list)
		min_col = max_col = 0
		queue = deque()
		queue.append((root, 0))

		while queue:
			p_node, col_idx = queue.popleft()

			if p_node:
				min_col = min(min_col, col_idx)
				max_col = max(max_col, col_idx)
				col_hashtable[col_idx].append(p_node.val)

				queue.append((p_node.left, col_idx - 1))
				queue.append((p_node.right, col_idx + 1))

		return [col_hashtable[col] for col in range(min_col, max_col + 1)]
