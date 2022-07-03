剑指 Offer 33. 二叉搜索树的后序遍历序列



# Divide and conquer
# recursion
# isValid(i, j) return if the series is a valid binary search tree
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def isValid(i, j):
            nonlocal postorder
            # j is the index of root node, since it is postorder travel
            # Base case
            if i >= j:
                return True

            p = i
            # find the left clid tree
            # mark the spliting position m
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            # go through the right child tree
            # the nodes in right cild tree should be smaller than root node
            # and the pointer p should be equal to j
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and isValid(i, m - 1) and isValid(m, j - 1)

        return isValid(0, len(postorder) - 1)