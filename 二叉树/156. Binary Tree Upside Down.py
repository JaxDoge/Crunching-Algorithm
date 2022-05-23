156. Binary Tree Upside Down


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# postorder travel
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root

        newRoot = root
        while newRoot.left is not None:
            newRoot = newRoot.left

        def postOrder(node, parent, rightFlag):
            if node is None:
                return
            if rightFlag and node.left is None and node.right is None:
                return

            postOrder(node.left, node, False)
            postOrder(node.right, node, True)

            node.right = parent
            if parent is not None:
                node.left = parent.right
            else:
                node.left = None
            return

        postOrder(root, None, False)
        return newRoot