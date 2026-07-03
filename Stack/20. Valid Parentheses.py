20. Valid Parentheses

# Stack
class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		hashmap = {
			')': '(',
			'}': '{',
			']': '['
			}
		
		for c in s:
			if c == ')' or c == '}' or c == ']':
				if not stack:
					return False
				elif stack.pop() != hashmap[c]:
					return False
				else:
					continue
			else:
				stack.append(c)

		return not stack