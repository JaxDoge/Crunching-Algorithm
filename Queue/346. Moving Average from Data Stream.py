346. Moving Average from Data Stream


class MovingAverage:

	def __init__(self, size: int):
		self.size = size
		self.sum = 0
		self.queue = deque()

	def next(self, val: int) -> float:
		if len(self.queue) >= self.size:
			self.sum -= self.queue[0]
			self.queue.popleft()

		self.queue.append(val)
		self.sum += val

		return self.sum / len(self.queue)