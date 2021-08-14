236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 后序遍历
# 对某一个根节点，如果它是lca,那么要满足
# p q 在它左右两个不同的子树上，或者一个是节点本身
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None 
        # there is no badcases for p and q, according to the constraints
        def backorder(node,p,q):
            if not node: return None 
            
            # 这也是一种 badcase，如果 node 就是 p 或者 q，直接返回这个节点，不需要继续迭代了，
            # 因为不论另一个节点是否在 node 的子树里，这个返回都是正确的
            if node == p or node == q: return node 

            left_search_res = backorder(node.left,p,q)
            right_search_res = backorder(node.right,p,q)

            # Situation 1, 目标 node 分别在左右子树，返回这个根节点
            if left_search_res and right_search_res:
                return node 

            # Situation 2, 目标节点都没有找到，返回空
            if not left_search_res and not right_search_res:
                return None  

            # Situation 3, 目标节点在 left_search_res 或 right_search_res 中有找到，用找到的那边代替 node 返回
            return left_search_res if not right_search_res else right_search_res
        return backorder(root,p,q)




