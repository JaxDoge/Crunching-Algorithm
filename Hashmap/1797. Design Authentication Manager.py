1797. Design Authentication Manager


class AuthenticationManager:

	def __init__(self, timeToLive: int):
		self.ttl = timeToLive
		self.auth_dict = {}

	def generate(self, tokenId: str, currentTime: int) -> None:
		self.auth_dict[tokenId] = currentTime + self.ttl


	def renew(self, tokenId: str, currentTime: int) -> None:
		if tokenId not in self.auth_dict:
			return

		if self.auth_dict[tokenId] <= currentTime:
			return

		self.auth_dict[tokenId] = currentTime + self.ttl
		

	def countUnexpiredTokens(self, currentTime: int) -> int:
		res = 0

		for exp in self.auth_dict.values():
			if exp > currentTime:
				res += 1

		return res
		


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)