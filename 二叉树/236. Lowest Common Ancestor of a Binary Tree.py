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

            # Situation 1, 目标 node 分别在左右子树，返回这个根节点，这是搜索结果逐层上传的一种结果，汇合
            if left_search_res and right_search_res:
                return node 

            # Situation 2
            return left_search_res or right_search_res
        return backorder(root,p,q)




class Solution:
    def _preorder(self, node, route: list, p, q, p_route, q_route):
        if not node:
            return

        route.append(node)
        if node == p:
            p_route.extend(route) 
        if node == q:
            q_route.extend(route)

        if p_route and q_route:
            return

        self._preorder(node.left, route, p, q, p_route, q_route)
        self._preorder(node.right, route, p, q, p_route, q_route)

        route.pop()


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_route = []
        q_route = []

        self._preorder(root, [], p, q, p_route, q_route)

        for p_node, q_node in zip(p_route, q_route):
            if p_node != q_node:
                break
            lca = p_node

        return lca