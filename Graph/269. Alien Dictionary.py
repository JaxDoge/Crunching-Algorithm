269. Alien Dictionary


from collections import defaultdict, Counter, deque

class Solution:
	def alienOrder(self, words: List[str]) -> str:

		# Create the graph and in_degree counter (with 0 in_degree initially)
		graph = defaultdict(set)
		in_degree = Counter({c: 0 for word in words for c in word})

		# Fill the graph and counter
		# If the second word is the prefix, then return ""
		for first_w, second_w in zip(words, words[1:]):
			for c, d in zip(first_w, second_w):
				if c != d:
					if d not in graph[c]:
						graph[c].add(d)
						in_degree[d] += 1
					break
			# If NOT BREAK, check incorrect prefix case
			else:
				if len(first_w) > len(second_w):
					return ""

		# BFS
		# Always find and extract the character with 0 in_degree
		res = []
		queue = deque([c for c in in_degree if in_degree[c] == 0])

		while queue:
			c = queue.popleft()
			res.append(c)
			for nb in graph[c]:
				in_degree[nb] -= 1
				if in_degree[nb] == 0:
					queue.append(nb)

		# Check if there is a loop
		# Not all characters have 0 indegree
		if len(res) < len(in_degree):
			return ""

		return "".join(res)

