662. Maximum Width of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# level order (BFS) to find out the depth of the tree
# compare the length of last level and the second last level
# the number of node in a given level is 2^n, except the last one
# for the last level, we have to find the last node with at least one child, and what child it is
# Then calculate the length of this layer
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1

        node = root

        # BFS
        from collections import deque

        queue = deque()
        queue.append([node, 1])
        ans = 1

        while queue:
            start = queue[0][1]
            end = queue[-1][1]
            width = end - start + 1
            ans = max(ans, end - start + 1)

            curLSize = len(queue)

            for i in range(curLSize):
                curNode, curID = queue.popleft()
                if curNode.left:
                    queue.append([curNode.left, curID * 2 - 1])

                if curNode.right:
                    queue.append([curNode.right, curID * 2])




        return ans

