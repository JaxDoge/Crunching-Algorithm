69. Sqrt(x)

# newton interpolation
class Solution:
	def mySqrt(self, x: int) -> int:
		if x == 0:
			return 0
		
		C, x0 = float(x), float(x)
		while True:
			xi = 0.5 * (x0 + C / x0)
			if abs(x0 - xi) < 1e-7:
				break
			x0 = xi
		
		return int(x0)


# Binary Search
class Solution:
	def mySqrt(self, x: int) -> int:
		if x == 1:
			return 1
			
		low = 1
		high = x // 2

		while low <= high:
			mid = (low + high) // 2
			mid_sqr = mid*mid
			if mid_sqr == x:
				return mid
			elif mid_sqr < x:
				low = mid + 1
			else:
				high = mid - 1

		return high