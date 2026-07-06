1249. Minimum Remove to Make Valid Parentheses


class Solution:
	def minRemoveToMakeValid(self, s: str) -> str:
		n = len(s)
		stack = []
		remove_set = set()

		for i in range(n):
			c = s[i]
			if c == '(':
				remove_set.add(i)
				stack.append((c, i))

			elif c == ')':
				if stack and stack[-1][0] == '(':
					remove_set.discard(stack[-1][1])
					stack.pop()
				else:
					remove_set.add(i)
					stack.append((c, i))

		res = []
		for i in range(n):
			if i in remove_set:
				continue
			res.append(s[i])

		return ''.join(res)