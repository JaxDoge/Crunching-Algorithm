126. Word Ladder II


# BFS
# I do note that the wordID dictionary is unnecessary
# and another virtual vectors set is needed
class Solution:
	def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
		word_graph = defaultdict(list)
		virtual_set = set()

		def addEdge(word):
			char_list = list(word)
			for i in range(len(char_list)):
				tmp = char_list[i]
				char_list[i] = '*'
				virtual_word = ''.join(char_list)
				virtual_set.add(virtual_word)
				word_graph[word].append(virtual_word)
				word_graph[virtual_word].append(word)
				char_list[i] = tmp
		
		for word in wordList:
			addEdge(word)

		if beginWord not in word_graph:
			addEdge(beginWord)

		if endWord not in word_graph:
			return []

		# Store the previous vectors in shortest path
		# So we don't need to store every partial path in the queue
		parents = defaultdict(list)
		# Record the shortest path length to reach every vector
		distance = {beginWord: 0}
		# Only store vector, not entire path
		queue = deque([beginWord])

		# BFS: queue nodes, not complete paths.
		while queue and endWord not in distance:
			for _ in range(len(queue)):
				word = queue.popleft()
				next_distance = distance[word] + 1

				for neighbor in word_graph[word]:
					if neighbor not in distance:
						distance[neighbor] = next_distance
						queue.append(neighbor)

					# Preserve every shortest way to reach neighbor.
					if distance[neighbor] == next_distance:
						parents[neighbor].append(word)

		if endWord not in distance:
			return []

		# Backtrack only through shortest-path parents.
		res = []
		path = [endWord]

		def backtrack(word):
			if word == beginWord:
				res.append([
					w for w in reversed(path)
					if w not in virtual_set
				])
				return

			for parent in parents[word]:
				path.append(parent)
				backtrack(parent)
				path.pop()

		backtrack(endWord)
		return res

