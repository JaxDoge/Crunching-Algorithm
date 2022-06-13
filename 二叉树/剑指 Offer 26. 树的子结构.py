剑指 Offer 26. 树的子结构



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# preorder travel
class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if not (A and B):
            return False

        # check if tree b is part of tree a
        # the root node of tree b must corresponding to the root node of tree a
        def isValid(a, b):
            if not b:
                return True
            elif not a or a.val != b.val:
                return False
            else:
                return isValid(a.left, b.left) and isValid(a.right, b.right)

        # Note that both A and B are not None, so the base case of isValid is different
        res = isValid(A, B)
        
        if res:
            return res
        # if this part of A tree is not valid, check whether the left and the right child tree of A
        # match B
        else:
            return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

