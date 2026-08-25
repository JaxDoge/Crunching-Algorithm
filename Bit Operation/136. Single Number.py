136. Single Number

# a⊕b⊕a=(a⊕a)⊕b=0⊕b=b

class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		res = 0
		for num in nums:
			res ^= num
		return res 
