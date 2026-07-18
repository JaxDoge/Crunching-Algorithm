863. All Nodes Distance K in Binary Tree



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Find the route to the target
# Find relay node (distance <= k), include the target
# Search each relay node, start from the one closest to the root
# Skip the child that already in the relay route

class Solution:
	def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
		relay = deque()
		res = []

		def preorder_relay(node, target, cur_path):
			nonlocal relay
			if not node:
				return

			cur_path.append(node)
			if node == target:
				relay = deque(cur_path)
				return

			preorder_relay(node.left, target, cur_path)
			preorder_relay(node.right, target, cur_path)

			cur_path.pop()		

		def preorder_res(node, avoid, dist):
			nonlocal res
			if not node:
				return

			if node == avoid:
				return

			if dist == 0:
				res.append(node.val)
				return

			preorder_res(node.left, avoid, dist - 1)
			preorder_res(node.right, avoid, dist - 1)

		# Find relays
		preorder_relay(root, target, [])


		while len(relay) > k + 1:
			relay.popleft()

		while relay:
			rest_k = k - len(relay) + 1
			top_node = relay.popleft()
			avoid = relay[0] if relay else None
			preorder_res(top_node, avoid, rest_k)

		return res

