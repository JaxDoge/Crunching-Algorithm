272. Closest Binary Search Tree Value II



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder traverse return the sorted list of all distinct values
class Solution:
	def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
		def inorder(node, arr):
			if not node:
				return
			inorder(node.left, arr)
			arr.append(node.val)
			inorder(node.right, arr)

		arr = []
		inorder(root, arr)

		# bisect can return as large as `n` (out of index) but as small as `0` (valid index)
		# We need at least one of left and right point to a valid index
		left = bisect_left(arr, target) - 1
		right = left + 1

		ans = deque()

		while len(ans) < k:
			if left < 0:
				ans.append(arr[right])
				right += 1
			elif right == len(arr):
				ans.append(arr[left])
				left -= 1
			elif abs(arr[left] - target) <= abs(arr[right] - target):
				ans.append(arr[left])
				left -= 1
			else:
				ans.append(arr[right])
				right += 1

		return list(ans)

