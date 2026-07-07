387. First Unique Character in a String



class Solution:
	def firstUniqChar(self, s: str) -> int:
		n = len(s)
		hashmap = {}
		queue = deque()

		for i in range(n):
			c = s[i]
			if c not in hashmap:
				hashmap[c] = 1
				queue.append(i)
			else:
				hashmap[c] += 1
				while queue and hashmap[s[queue[0]]] > 1:
					queue.popleft()


		return queue[0] if queue else -1