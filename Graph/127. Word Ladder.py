127. Word Ladder

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


# BFS + 虚拟节点优化建图
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    	import collections
    	wordID = dict()
    	edge_dict = collections.defaultdict(list)
		# 给每个词编码 id ，从 0 开始
    	wordid_num = 0

    	# 构建词编码字典
    	def addWord(word: str):
    		nonlocal wordid_num
    		if word not in wordID:
    			wordID[word] = wordid_num
    			wordid_num += 1

    	# 每个词构建对应的虚拟联通节点，加入图中
    	def addEdge(word: str):
    		# 先加入词字典
    		addWord(word)
    		# 获取该词编码
    		id_1 = wordID[word]
    		# 将该词列表化
    		chars = list(word)
    		# 循环替代每个字母，生成对应的图 vector
    		for ch in range(len(chars)):
    			# 记录被替换的字母，之后换回去
    			tmp = chars[ch]
    			chars[ch] = '*'
    			# 生成新词，加入词字典
    			newWord = ''.join(chars)
    			addWord(newWord)
    			id_2 = wordID[newWord]
    			# 联通原词和新词
    			edge_dict[id_1].append(id_2)
    			edge_dict[id_2].append(id_1)

    			chars[ch] = tmp

    	# 构造词图
    	for word in wordList:
    		addEdge(word)
        if beginWord not in edge_dict:
            addEdge(beginWord)
            
    	# Badcase，endWord 不在词字典中，完全不可能连接，用哈希表判断比原始 list 快
    	if endWord not in wordID:
    		return 0

        helper_queue = collections.deque()
        #路径长度初始化为1,因为 beginWord 必在其中
    	path = 1
    	beginID, endID = wordID[beginWord], wordID[endWord]
        helper_queue.append(beginID)
        # visited 避免重复访问
        visited = collections.defaultdict()

        while helper_queue:
        	subsize = len(helper_queue)
        	for _ in range(subsize):
        		popID = helper_queue.popleft()
        		visited[popID] = None
        		# 成功联通，路径长度因为存在虚拟vector 层，实际应为 (x+1)/2
        		if popID == endID:
        			return (path+1)>>1
        		for next_wordID in edge_dict[popID]:
        			if next_wordID not in visited:
        				helper_queue.append(next_wordID)

        	# 遍历完当前层
        	path += 1
        return 0


# 双向 BFS，前提是明确知道起点和终点是哪两个节点

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    	import collections
    	wordID = dict()
    	edge_dict = collections.defaultdict(list)
		# 给每个词编码 id ，从 0 开始，这个值代表了 wordID 字典中的词总数
    	wordid_num = 0

    	# 构建词编码字典
    	def addWord(word: str):
    		nonlocal wordid_num
    		if word not in wordID:
    			wordID[word] = wordid_num
    			wordid_num += 1

    	# 每个词构建对应的虚拟联通节点，加入图中
    	def addEdge(word: str):
    		# 先加入词字典
    		addWord(word)
    		# 获取该词编码
    		id_1 = wordID[word]
    		# 将该词列表化
    		chars = list(word)
    		# 循环替代每个字母，生成对应的图 vector
    		for ch in range(len(chars)):
    			# 记录被替换的字母，之后换回去
    			tmp = chars[ch]
    			chars[ch] = '*'
    			# 生成新词，加入词字典
    			newWord = ''.join(chars)
    			addWord(newWord)
    			id_2 = wordID[newWord]
    			# 联通原词和新词
    			edge_dict[id_1].append(id_2)
    			edge_dict[id_2].append(id_1)

    			chars[ch] = tmp

    	# 构造词图
    	for word in wordList:
    		addEdge(word)

    	addEdge(beginWord)
    	# Badcase，endWord 不在词字典中，完全不可能连接，用哈希表判断比原始 list 快
    	if endWord not in wordID:
    		return 0

        # 从两头同时出发
    	disBegin = [float('inf')] * wordid_num
    	beginID = wordID[beginWord]
    	disBegin[beginID] = 1
        helper_queue_begin = collections.deque([beginID])

        disEnd = [float('inf')] * wordid_num
        endID = wordID[endWord]
        disEnd[endID] = 1
        helper_queue_end = collections.deque([endID])

        while helper_queue_begin or helper_queue_end:
        	subBeginSize = len(helper_queue_begin)
        	for _ in range(subBeginSize):
        		popID = helper_queue_begin.popleft()
        		# 进队列的节点均已计算完连线起点的节点数
        		# 如果该节点已经在另一侧也被搜索过，也记录了和另一侧的距离，则两端联通，返回结果
        		if disEnd[popID] != float('inf'):
        			return (disBegin[popID]+disEnd[popID])>>1  # 纸面距离应该是求和-1，但由于存在虚拟节点，直接变成了/2
        		for nextNode in edge_dict[popID]:
        			if disBegin[nextNode] == float('inf'): # 没有对应距离，则没有被搜索过，反之则反之
	        			disBegin[nextNode] = disBegin[popID] + 1
	        			helper_queue_begin.append(nextNode)

        	subEndSize = len(helper_queue_end)
			for _ in range(subEndSize):
        		popID = helper_queue_end.popleft()
        		if disBegin[popID] != float('inf'):
        			return (disBegin[popID]+disEnd[popID])>>1  # 纸面距离应该是求和-1，但由于存在虚拟节点，直接变成了/2
        		for nextNode in edge_dict[popID]:
        			if disEnd[nextNode] == float('inf'):
	        			disEnd[nextNode] = disEnd[popID] + 1
	        			helper_queue_end.append(nextNode)        	
        return 0






