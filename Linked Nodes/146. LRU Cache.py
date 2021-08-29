146. LRU Cache

class ListNode:
    def __init__(self, val = 0, key = 0, next: ListNode = None, previous: ListNode = None):
        self.val = val 
        self.key = key
        self.next = next 
        self.previous = previous 


class LRUCache:

    def __init__(self, capacity: int):
        import collections
        self.size = capacity
        # The key of dict is the original key, but the value of the dict is the corresponding node
        self.nodedict = collections.defaultdict(ListNode)   
        self.dummy_head = ListNode(val = -1)
        self.dummy_end = ListNode(val = -1)   # Should point to the end of list
        self.dummy_head.next = self.dummy_end
        self.dummy_end.previous = self.dummy_head

    def get(self, key: int) -> int:
        if not key in self.nodedict:
            return -1
        else:
            get_node = self.nodedict[key]
            # move the node to the top
            if self.dummy_head.next != get_node:
                get_node.previous.next = get_node.next 
                get_node.next.previous = get_node.previous

                get_node.next = self.dummy_head.next  
                get_node.previous = self.dummy_head
                get_node.next.previous = get_node
                self.dummy_head.next = get_node  
            return get_node.val



    def put(self, key: int, value: int) -> None:
        if key in self.nodedict:
            self.nodedict[key].val = value
            # 这里也要调整node位置呀！！！！
            get_node = self.nodedict[key]
            # move the node to the top
            if self.dummy_head.next != get_node:
                get_node.previous.next = get_node.next 
                get_node.next.previous = get_node.previous

                get_node.next = self.dummy_head.next  
                get_node.previous = self.dummy_head
                get_node.next.previous = get_node
                self.dummy_head.next = get_node              
            return
        # create new node at the head
        new_node = ListNode(val = value, key = key)
        new_node.next = self.dummy_head.next
        new_node.previous = self.dummy_head
        new_node.next.previous = new_node
        self.dummy_head.next = new_node 
        # record the new node in the dictionary
        self.nodedict[key] = new_node  

        if len(self.nodedict) > self.size:
            # evict the end node
            end_node = self.dummy_end.previous
            end_node.previous.next = end_node.next 
            end_node.next.previous = end_node.previous

            end_node.next = end_node.previous = None 
            del self.nodedict[end_node.key]

            return

        else:
            return




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

