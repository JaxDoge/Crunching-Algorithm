146. LRU Cache

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _append_to_tail(self, node: Node):
        old_last = self.tail.prev
        old_last.next = node
        node.prev = old_last

        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]

        self._remove_node(node)
        self._append_to_tail(node)

        return node.value

        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self._remove_node(node)
            self._append_to_tail(node)
            return

        if len(self.hashmap) >= self.capacity:
            lru_node = self.head.next

            self._remove_node(lru_node)
            del self.hashmap[lru_node.key]
        
        new_node = Node(key, value)
        self.hashmap[key] = new_node
        self._append_to_tail(new_node)
        



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