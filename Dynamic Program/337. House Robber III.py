337. House Robber III


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        res = self.dp(root)
        return max(res)

    def dp(self, root):
        if not root:
            return [0, 0]
        left = self.dp(root.left)
        right = self.dp(root.right)
        rob_root = root.val + left[0] + right[0]
        dont_rob = max(left) + max(right)
        return [dont_rob, rob_root]