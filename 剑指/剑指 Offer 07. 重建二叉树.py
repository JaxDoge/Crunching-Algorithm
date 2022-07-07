剑指 Offer 07. 重建二叉树



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        n = len(preorder)

        def btRecursion(pStart, pEnd, iStart, iEnd):
            nonlocal preorder, inorder, n
        
            if pEnd - pStart == 1:
                return TreeNode(preorder[pStart])

            # find the root node in inorder
            # and split the left and right child tree

            rootVal = preorder[pStart]
            root = TreeNode(rootVal)

            for i in range(iStart, iEnd):
                if inorder[i] == rootVal:
                    break

            # the length of left child series
            leftLength = i - iStart

            # if left child exists
            if leftLength > 0:
                root.left = btRecursion(pStart + 1, pStart + 1 + leftLength, iStart, i)

            # if right child exists
            if i < iEnd - 1:
                root.right = btRecursion(pStart + 1 + leftLength, pEnd, i + 1, iEnd)

            return root


        return btRecursion(0, n, 0, n)
