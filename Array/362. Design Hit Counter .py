362. Design Hit Counter

# Remember the input timestamp is monotonic increasing. So we only need to counter the `latest` situation

class HitCounter:

	def __init__(self):

		self.total = 0
		self.hits = deque()
		

	def hit(self, timestamp: int) -> None:
		# case 1, insert a new hit item
		if not self.hits or self.hits[-1][0] != timestamp:
			self.hits.append([timestamp, 1])
		else:
			self.hits[-1][1] += 1
		self.total += 1

	def getHits(self, timestamp: int) -> int:
		retro_limit = 300
		
		while self.hits:
			diff = timestamp - self.hits[0][0]
			if diff >= retro_limit:
				self.total -= self.hits[0][1]
				self.hits.popleft()
			else:
				# all hit records happened in 5 minutes
				break

		return self.total