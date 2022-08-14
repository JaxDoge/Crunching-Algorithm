1740. Find Distance in a Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0 

        # find the length from node to target
        def dfs(node, target):
            if not node.next:
                return -1

            if node.val == target:
                return 0

            lChild = dfs(node.left, target)
            rChild = dfs(node.right, target)

            if lChild == rChild == -1:
                return -1

            return max(lChild, rChild) + 1

        # find the LCA
        def lcaPostorder(node, p, q):
            if not node:
                return 

            if node.val in {p, q}:
                return node 

            lSearch = lcaPostorder(node.left, p, q)
            rSearch = lcaPostorder(node.right, p, q)

            # case 1
            if lSearch and rSearch:
                return node

            # case 2
            if not lSearch and not rSearch:
                return None 

            # case 3
            return lSearch if not rSearch else rSearch



        lca = lcaPostorder(root, p, q)
        res = dfs(lca, p) + dfs(lca, q)

        return res
