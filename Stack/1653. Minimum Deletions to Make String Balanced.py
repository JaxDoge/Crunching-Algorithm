1653. Minimum Deletions to Make String Balanced


# Need to find the number of "unbalanced pairs" (b, a)

class Solution:
	def minimumDeletions(self, s: str) -> int:
		stack = []
		res = 0

		for c in s:
			if c == 'b':
				stack.append(c)
			else:
				# c is a
				# Check the top of stack
				if stack:
					top_c = stack[-1]
					if top_c == 'b':
						stack.pop()
						res += 1
						continue

				stack.append(c)

		return res
		