25. Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# 递归解法，空间复杂度 O(n)
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    	# basd case 1
    	if not head: return head 
    	start = end = head 
        # badcase 2, Noting that the return condition judgement is ahead of the end movement
    	for _ in range(k):
            if not end: return head 
            end = end.next 
        
        # new_head point to the head of reversed sublist
        new_head = self.subReverse(start, end)
        # the start.next should point to the head of next sublist(reversed or not), not null
        start.next = self.reverseKGroup(end, k)
        return new_head

    
    # reverse node in [head, end)
    def subReverse(self, head, end):
    	pre = None 
    	cur = next_node = head 
    	while cur != end:
    		next_node = cur.next 
    		cur.next = pre   
    		pre = cur  
    		cur = next_node

    	return pre 



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



        