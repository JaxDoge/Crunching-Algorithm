328. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
    	if not head or not head.next: return None
    	# add dummy end node
    	odd = head
    	even = head.next
    	even_head = even

    	while even and even.next:  # if the length is a even number, stop when even pointer at the last node
    	    odd.next = even.next
    	    odd = odd.next
    	    even.next = odd.next
    	    even = even.next   # which is the odd.next 
    	odd.next = even_head
    	return head

    	


