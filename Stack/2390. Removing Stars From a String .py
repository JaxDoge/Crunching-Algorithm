2390. Removing Stars From a String


# Classic stack usage

class Solution:
	def removeStars(self, s: str) -> str:
		n = len(s)
		stack = []

		for c in s:
			if c == "*":
				stack.pop()
			else:
				stack.append(c)

		return "".join(stack)		