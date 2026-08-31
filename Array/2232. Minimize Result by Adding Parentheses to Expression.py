2232. Minimize Result by Adding Parentheses to Expression

# Brutal Force
# Find the "+"
class Solution:
	def minimizeResult(self, expression: str) -> str:
		n = len(expression)
		res = float('inf')
		ans = ''

		plus_idx = -1
		for i in range(n):
			if expression[i] == '+':
				plus_idx = i
				break

		for left in range(plus_idx - 1, -1, -1):
			for right in range(plus_idx + 1, n, 1):
				l_multiplier = 1 if left == 0 else int(expression[:left])
				r_multiplier = 1 if right == n - 1 else int(expression[right + 1:])

				l_addend = int(expression[left:plus_idx])
				r_addend = int(expression[plus_idx + 1: right + 1])

				cur_output = (l_addend + r_addend) * l_multiplier * r_multiplier
				if cur_output < res:
					ans = expression[:left] + '(' + expression[left:right + 1] + ')' + expression[right + 1:]
					res = cur_output

		return ans


