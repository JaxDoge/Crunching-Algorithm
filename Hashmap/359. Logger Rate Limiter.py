359. Logger Rate Limiter


class Logger:

	def __init__(self):
		self.message_dict = defaultdict(int)
		

	def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
		if message not in self.message_dict or self.message_dict[message] <= timestamp:
			self.message_dict[message] = timestamp + 10
			return True

		return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)