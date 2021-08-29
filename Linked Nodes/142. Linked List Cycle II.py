142. Linked List Cycle II


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Hash table
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
    	if not head: return None 
    	if not head.next: return None 

    	 
    	memo = set()

    	cur = head  
    	while cur:
    		if cur in memo:
    			return cur
    		else:
    			memo.add(cur)
    		cur = cur.next 
        return None


# 快慢指针
# fast 走的步数是slow步数的 2 倍，即 f = 2s；（解析： fast 每轮走 22 步）
# fast 比 slow多走了 nn 个环的长度，即 f = s + nb；（ 解析： 双指针都走过 aa 步，然后在环内绕圈直到重合，重合时 fast 比 slow 多走 环的长度整数倍 ）；
# 以上两式相减得：f = 2nbf=2nb，s = nbs=nb，即fast和slow 指针分别走了 2n2n，nn 个 环的周长 （注意： nn 是未知数，不同链表的情况不同）。


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
    	if not head: return None 
    	if not head.next: return None 

    	p = q = head  # pq 起点必须相同，否则公式 f = s + nb 不成立，变成了 f= s-1 +nb  
    	  

    	while q.next and q.next.next:
    		# 移动必须发生在判定前面，因为一开始两个指针就是相遇的
    	    p = p.next
    	    q = q.next.next     		
    	    if q == p:

    	    	# Get the special index
    	    	r = head 
    	    	while r != p:
    	    		r = r.next 
    	    		p = p.next 
    	    	return r


        return None    	



