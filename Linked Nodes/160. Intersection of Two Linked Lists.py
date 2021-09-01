160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Hash Table, space O(n) (if n>m)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    	node_memo = set()
    	cur1 = headA
    	cur2 = headB

    	while True:
    		if cur1 == None: break
    		node_memo.add(cur1)
    		cur1 = cur1.next 

    	while True:
    		if cur2 == None: break 
    		if cur2 in node_memo:
    			return cur2
    		else:
    			node_memo.add(cur2)
    			cur2 = cur2.next
    	return None


# Double pointers, space O(1)
# 关键思路是两个指针分别走一遍对方的前半段节点，可以消除路径的不相同，必然在交汇节点相遇, 或者同时在对方的链表遍历结束

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        cur1 = headA
        cur2 = headB

        while True:
        	# 优先判断是否相同，考虑只有一个节点的情况，也包含了没有节点的情况
            if cur1 == cur2:
                return cur1
            # 遍历完成如果没有交集，因该满足的条件的两个指针的下一个都为空，而不是本身为空，因为按步骤本身永远不会为空
            if not cur1.next and not cur2.next: break             
            if cur1 and cur2:
                cur1 = cur1.next
                cur2 = cur2.next
            if not cur1:
                cur1 = headB
            if not cur2:
                cur2 = headA

        return None