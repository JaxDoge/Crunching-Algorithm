25. Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def reverseLinkList(self, start, end):
		pre = None
		cur = next_node = start
		while cur != end:
			next_node = cur.next
			cur.next = pre
			pre = cur
			cur = next_node

		return pre
		

	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		if k == 1:
			return head
		# find successor
		if not head:
			return head
		end = head
		for _ in range(k - 1):
			end = end.next
			if not end:
				return head
		
		end = end.next
		new_head = self.reverseLinkList(head, end)
		head.next = self.reverseKGroup(end, k)
		return new_head



# 迭代解法，可以先断开 end 与后面节点的链接，然后把 start 传入 subReverse，这样就少一个参数传入
class Solution:
	def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
		# Bad case: reach the None node or the end node
		if not head or not head.next:
			return head 
		# dummy head 
		dummy_head = ListNode(val = -1, next = head)
		pre = end = dummy_head

		while end:
			# move end to the end of to-reverse sublist
			for _ in range(k):
				if not end: break
				end = end.next 
				# print(end.val)
			if not end: break
				

			start = pre.next 
			successor = end.next 
			# break the link of end 
			end.next = None 
			# Reverse sublist and re-link
			pre.next = self.subReverse(start)
			start.next = successor

			# redefine flags
			pre = end = start 
		return dummy_head.next 

	# reverse a sub-linknode from start and return the new head node
	def subReverse(self, start):
		pre = None 
		cur = next_node = start 
		while cur:
			next_node = cur.next 
			cur.next = pre 
			pre = cur 
			cur = next_node

		return pre  



		