24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# 递归解法
class Solution:
    # def __init__(self, head: ListNode):
    # 	self.dummy_head = ListNode(val = -1, next = head)

    def swapPairs(self, head: ListNode) -> ListNode:
    	if not head or not head.next:
    		return head
    	successor = head.next.next 
    	new_head = head.next
    	head.next.next = head
    	head.next = self.swapPairs(successor)
    	return new_head


# 迭代解法

class Solution:
	def swapPairs(self, head: ListNode) -> ListNode:
		if not head or not head.next:
			return head 

		dummy_head = ListNode(val = -1, next = head)

		pre = dummy_head
		 

		while head and head.next:
			next_node = head.next
			pre.next = next_node
			head.next = next_node.next 
			next_node.next = head 

			pre = head
			head = head.next

        
        return dummy_head.next 

