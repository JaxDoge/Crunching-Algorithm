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
        
        #这里的逻辑不专业，应该先判断linkedhashmap 大小，再决定是否删除，再插入新节点
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






# More professional design

class Node:
    def __init__(self, val = 0, key = 0, next = None, previous = None):
        self.val = val 
        self.key = key
        self.next = next
        self.previous = previous 

class Doublelist:
    def __init__(self, size_=0):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.size = size_

    # 双链表的一些基本 API
    # 在链表尾部添加节点 x，时间 O(1)
    def addLast(self, node: Node):
        node.previous = self.tail.previous
        self.tail.previous = node
        node.previous.next = node
        node.next = self.tail
        self.size += 1

    # 删除并返回某个节点，该节点已经确定存在与列表中
    def remove(self, node: Node):
        node.previous.next = node.next
        node.next.previous = node.previous
        node.previous = None
        node.next = None
        self.size -= 1
    
    # 删除链表第一个节点并返回
    def removeFirst(self):
        if self.head.next == self.tail: return None
        first_node = self.head.next
        self.remove(first_node)
        return first_node

    def get_size(self):
        return self.size

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = Doublelist()
        self.map = dict()

    # 中间封装若干 API，统一操作
    # 将某个 key 提升为最近使用的
    def promotRecent(self, key_):
        node = self.map[key_]
        self.cache.remove(node)
        self.cache.addLast(node)

    # 添加新 kv 
    def addNewElement(self, key_: int, value_: int):
        node = Node(key = key_, val = value_)
        self.cache.addLast(node)
        self.map[key_] = node

    # 删除某个 key
    def deleteKey(self, key_: int):
        node = self.map[key_]
        # 从链表中删除
        self.cache.remove(node)
        # 从hashmap 中删除
        del self.map[key_]

    # 删除最久未使用的元素
    def deleteLastRecent(self):
        node = self.cache.removeFirst()
        # 别忘了在hashmap里也要删除
        key = node.key
        del self.map[key]

    # 开始搞正式的 API
    def get(self, key_: int):
        # 如果不存在
        if not key_ in self.map:
            return -1

        self.promotRecent(key_)
        return self.map[key_].val

    def put(self, key_:int, value_: int):
        if key_ in self.map:
            # 删除旧节点，空间足够
            self.deleteKey(key_)
            # 新增元素
            self.addNewElement(key_, value_)
            return

        # 判断空间是否足够
        if self.cache.size >= self.cap:
            # 删除LRU元素
            self.deleteLastRecent()

        self.addNewElement(key_, value_)
        return