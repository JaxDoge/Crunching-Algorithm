67. Add Binary


# Not that easy actually
# 
from collections import deque
class Solution:
	def addBinary(self, a: str, b: str) -> str:
		ans = deque()
		n = max(len(b), len(a))
		carry = 0

		for i in range(n):
			carry += int(a[len(a)-1-i]) if i < len(a) else 0
			carry += int(b[len(b)-1-i]) if i < len(b) else 0
			ans.appendleft(str(carry % 2))
			carry = carry >> 1

		if carry > 0:
			ans.appendleft(str(carry))

		return ''.join(ans)



# More general
class Solution:
	def addBinary(self, a: str, b: str) -> str:
		m, n = len(a), len(b)
		carry = 0
		p = m - 1
		q = n - 1
		res = deque()

		while p > -1 and q > -1:
			cur_sum = int(a[p]) + int(b[q]) + carry
			carry, cur_sum = divmod(cur_sum, 2)
			res.appendleft(str(cur_sum))
			p -= 1
			q -= 1
		
		while p > -1:
			cur_sum = int(a[p]) + carry
			carry, cur_sum = divmod(cur_sum, 2)
			res.appendleft(str(cur_sum)) 
			p -= 1

		while q > -1:           
			cur_sum = int(b[q]) + carry
			carry, cur_sum = divmod(cur_sum, 2)
			res.appendleft(str(cur_sum))
			q -= 1
		
		if carry:
			res.appendleft(str(carry))

		return ''.join(res)


