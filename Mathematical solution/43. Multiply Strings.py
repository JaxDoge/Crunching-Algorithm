43. Multiply Strings

#  mimic pre-algebra multiplication, multiply by digits
#  double pointers
#  num1[i] * num2[j] return the part result in res[i+j] and res[i+j+1]
class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		# Bad case
		if num1 == '0' or num2 == '0':
			return '0'
		m = len(num1)
		n = len(num2)
		# the final outcome won't have more than m + n digits
		res = [0] * (m + n)
		# start from the right most index
		for i in range(m-1, -1, -1):
			for j in range(n-1, -1, -1):
				sub_res = int(num1[i]) * int(num2[j])
				#  find the corresponding res indices
				p1 = i + j
				p2 = p1 + 1
				sub_sum = sub_res + res[p2]
				# get carrier
				res[p2] = sub_sum % 10
				res[p1] = res[p1] + sub_sum // 10

		# find the left most non-zero index
		i = 0
		while i < len(res) and res[i] == 0:
			i += 1

		return ''.join([str(x) for x in res[i:]])



class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		if num1 == '0' or num2 == '0':
			return '0'

		m = len(num1)
		n = len(num2)

		res = deque()


		for j in range(n):
			carry = 0
			sub_res = deque()

			if res:
				res.append(0)

			for i in range(m - 1, -1, -1):
				prod = int(num1[i]) * int(num2[j]) + carry
				carry, prod = divmod(prod, 10)
				sub_res.appendleft(prod)

			if carry:
				sub_res.appendleft(carry)

			# Add sub_res to res
			if sub_res:
				self.add_lists(res, sub_res)

		return ''.join([str(num) for num in res])


	def add_lists(self, res, sub_res):
		if not res:
			res.extend(sub_res)
			return

		sub_len = len(sub_res)
		res_len = len(res)
		if sub_len > res_len:
			raise

		carry = 0
		k = sub_len - 1
		l = res_len - 1
		while k > -1 and l > -1:
			sumup = sub_res[k] + res[l] + carry
			carry, sumup = divmod(sumup, 10)
			res[l] = sumup
			k -= 1
			l -= 1

		while l > -1 and carry:
			sumup = res[l] + carry
			carry, sumup = divmod(sumup, 10)
			res[l] = sumup
			l -= 1

		if carry:
			res.appendleft(carry)

