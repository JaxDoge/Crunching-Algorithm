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











