1650. Lowest Common Ancestor of a Binary Tree III


"""
# Definition for a Node.
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None
"""

class Solution:
	def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
		p_parents = set()

		# p to root
		while p:
			p_parents.add(p)
			p = p.parent

		# q to root
		while q:
			if q in p_parents:
				return q
			q = q.parent