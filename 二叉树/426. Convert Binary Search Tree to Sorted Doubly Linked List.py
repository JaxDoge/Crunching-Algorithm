426. Convert Binary Search Tree to Sorted Doubly Linked List



"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        # find the head of double linked list
        head = root
        while head.left:
            head = head.left

        def rotation(node):
            if not node.left and not node.right:
                return (node, node)

            if node.left:
                hl, tl = rotation(node.left)
                tl.right = node
                node.left = tl
            else:
                hl = node

            if node.right:
                hr, tr = rotation(node.right)
                node.right = hr
                hr.left = node
            else:
                tr = node

            return (hl, tr)
        l, r = rotation(root)
        r.right = l
        l.left = r
        return head

