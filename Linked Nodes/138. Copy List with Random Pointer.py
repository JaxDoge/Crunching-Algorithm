138. Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
    	# Badcase
    	if not head:
    		return None 
    	if not head.next:
    		new_head = Node(x = head.val)
    		if head.random:
    			new_head.random = new_head
    		return new_head 

    	cur = head  
    	dummy_head = Node(x = 0)

        # Generate a simple linked Node, link new node at the next pointer of the original one
    	while cur:
    		new_node = Node(x = cur.val)
    		o_next = cur.next
    		cur.next = new_node
    		new_node.next = o_next 
    		cur = o_next 

    	cur = head 
    	new_cur = head.next 

        # Create corresponding random link, cur alway has next
    	while cur:
    		if cur.random:
    			new_cur.random = cur.random.next 

    		cur = new_cur.next 
    		if cur:
    		    new_cur = cur.next

    	cur = head 
    	new_cur = dummy_head

    	# delink two list:

    	while cur:
    		new_cur.next = cur.next 
    		cur.next = cur.next.next 

    		cur = cur.next 
    		new_cur = new_cur.next
        
        return dummy_head.next 


