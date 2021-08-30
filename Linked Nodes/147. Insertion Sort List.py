147. Insertion Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 插入排序，不是冒泡排序
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
    	if not head or not head.next: return head 

    	dummy_head = pre = ListNode(val = -99999, next = head)    # val could be zero since we won't use the value
    	last_sorted_node = head
    	cur = head.next 

    	while True:
    		if not cur: break 
    		if last_sorted_node.val <= cur.val:   # No operation need
    			last_sorted_node = cur
    		else:   # We need insert the cur node into the first n sorted nodes(end at last_sorted node)
    		    # relase a navigator
    		    pre_insert_node = dummy_head
    		    while True:
    		        if pre_insert_node.next.val >= cur.val: break
    		        pre_insert_node = pre_insert_node.next

    			last_sorted_node.next = cur.next
    			cur.next = pre_insert_node.next
    			pre_insert_node.next = cur

    		cur = last_sorted_node.next

 		return dummy_head.next





