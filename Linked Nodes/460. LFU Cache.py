460. LFU Cache

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


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

import collections
class LFUCache:

    def __init__(self, capacity: int):
    	self.key_val = dict()
    	self.key_freq = dict()
    	self.freq_key = dict()
    	self.cap = capacity
    	self.minFreq = 0


    def get(self, key: int) -> int:
    	if not key in self.key_val:
    		return -1

    	self.increaseFreq(key)
    	return self.key_val[key]


    def put(self, key: int, value: int) -> None:
    	if self.cap <= 0: return

    	# 若 KEY 已经存在，修改三个字典即可，无容量判断
    	if key in self.key_val:
    		self.key_val[key] = value
    		self.increaseFreq(key)
    		return

    	# 若 KEY 不存在，先判断容量，再加入新值
    	# 若容量已满，删除 freq 最小，最旧的 key 值
    	if self.cap <= len(self.key_val):
    		self.removeLeastFreq()

		self.key_val[key] = value
		self.key_freq[key] = 1
		if not 1 in self.freq_key:
			self.freq_key[1] = collections.OrderedDict()
		self.freq_key[1][key] = None  # 没必要加 value 
		self.minFreq = 1 # 新 key freq 必为最小的1

	def removeLeastFreq(self):
		# freq 最小的 key 列表
		key_set = self.freq_key[self.minFreq]
		deletekey, _ = key_set.popitem(last=False)
		# 如果 key_set 就这一个 key
		if not key_set:
			del self.freq_key[self.minFreq]
        del self.key_val[deletekey]
        del self.key_freq[deletekey]

	def increaseFreq(self, key):
		# 原 freq
		freq_ = self.key_freq[key]
		# 更新 FK KF 两个map
		self.key_freq[key] = freq_ + 1
		del self.freq_key[freq_][key]
		if not self.freq_key[freq_]:
			del self.freq_key[freq_]
			if self.minFreq == freq_:
				self.minFreq += 1
		if not freq_+1 in self.freq_key:
			self.freq_key[freq_+1] = collections.OrderedDict()
		self.freq_key[freq_+1][key] = None

