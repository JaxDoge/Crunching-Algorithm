1071. Greatest Common Divisor of Strings

# If the GCD string (str_gcd) exists, there must be a equation: GCD(len(str1), len(str2)) = len(str_gcd)

class Solution:
	def gcd(self, a: int, b:int):
		while b != 0:
			a, b = b, a % b
		return abs(a)

	def gcdOfStrings(self, str1: str, str2: str) -> str:
		len1 = len(str1)
		len2 = len(str2)

		str_gcd_len = self.gcd(len1, len2)

		if str1 + str2 != str2 + str1:
			return ""

		return str1[:str_gcd_len]