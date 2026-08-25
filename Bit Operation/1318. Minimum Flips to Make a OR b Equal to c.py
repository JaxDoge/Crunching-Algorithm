1318. Minimum Flips to Make a OR b Equal to c

# Check the least significant bit for three of them
class Solution:
	def minFlips(self, a: int, b: int, c: int) -> int:
		res = 0
		# if a and b and c are 0, the loop can be ended
		while a or b or c:
			
			if c & 1:
				# If a & 1 or b & 1 is 1 
				res += 0 if (a&1 or b&1) else 1
			else:
				# Both have to be ZERO
				res += (a&1) + (b&1)

			a >>= 1
			b >>= 1
			c >>= 1
		return res