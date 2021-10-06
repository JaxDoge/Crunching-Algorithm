710. Random Pick with Blacklist

# 由于 n 非常大，不能直接构建白名单
# 相应的 Blacklist 长度比较小
# 构建新的映射，把黑名单的数对应的索引映射到后半部分的白名单数字
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
    	self.white_list_size = n - len(blacklist)
    	self.black_mapping = dict()
    	# 初始化字典
    	for b in blacklist:
    		self.black_mapping[b] = 0

    	last_index = n - 1
    	for b in blacklist:
    		# 从最后一个索引开始遍历，如果对应的数已经是黑名单的数，跳过该索引
    		# 如果 b 已经落入【后半部份】区间，跳过 b
    		if b >= self.white_list_size:
    			continue
    		while last_index in self.black_mapping:
    			last_index -= 1
    		self.black_mapping[b] = last_index
    		last_index -= 1



    def pick(self) -> int:
    	import random
    	rand = random.randrange(self.white_list_size)
    	if rand in self.black_mapping:
    		return self.black_mapping[rand]
    	return rand


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()