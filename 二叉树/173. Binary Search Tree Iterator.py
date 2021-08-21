173. Binary Search Tree Iterator


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stack.pop()
        node = cur.right
        while node:  # if cur has right node
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

作者：lcbin
链接：https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/doocskai-yuan-she-qu-python3-java-c-go-d-ohom/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()