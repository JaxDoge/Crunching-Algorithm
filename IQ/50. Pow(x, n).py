50. Pow(x, n)


# Quick pow
class Solution:
	def myPow(self, x: float, n: int) -> float:
		if n == 0:
			return 1
		# convert n to positive
		revFlag = False
		if n < 0:
			revFlag = True
			n = abs(n)

		ans = self.helper(x, n, 1)
		if revFlag:
			return 1/ans
		return ans

	def helper(self, x, n, res):
		if n == 1:
			return x * res

		if n % 2 == 1:
			res *= x
		
		x = x*x
		n = n // 2
		return self.helper(x, n, res)


class Solution:
	def myPow(self, x: float, n: int) -> float:
		if x == 0:
			return 0
		if n == 0:
			return 1

		if n % 2 != 0 and x < 0:
			sign = -1
			x = -x
		else:
			sign = 1

		if abs(x) == 1:
			return 1 * sign

		reciprocal = False
		if n < 0:
			reciprocal = True
			n = - n

		def quickProd(val, cur_pow):
			if cur_pow * 2 > n:
				return val, cur_pow

			return quickProd(val * val, cur_pow * 2)

		res = 1

		while n > 0:
			cur_pow = 1            
			tmp_val, cur_pow = quickProd(x, cur_pow)
			res *= tmp_val
			n -= cur_pow

		res *= sign

		return res if not reciprocal else 1/res