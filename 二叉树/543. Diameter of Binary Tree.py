543. Diameter of Binary Tree




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Postorder traveler
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def postorder(node):
            nonlocal res
            if node.left is None and node.right is None:
                return [0, 0]

            if node.left:
                leftE = max(postorder(node.left)) + 1
            else:
                leftE = 0

            if node.right:
                rightE = max(postorder(node.right)) + 1
            else:
                rightE = 0

            res = max(res, leftE + rightE)
            return [leftE, rightE]

        postorder(root)
        
        return res



