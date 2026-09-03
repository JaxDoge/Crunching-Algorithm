17. Letter Combinations of a Phone Number

# Backtrack

DAIL_ALPH = {
	2:['a','b','c'],
	3:['d','e','f'],
	4:['g','h','i'],
	5:['j','k','l'],
	6:['m','n','o'],
	7:['p','q','r','s'],
	8:['t','u','v'],
	9:['w','x','y','z']

}


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		n = len(digits)
		res = []
		comb = []

		def findComb(idx):
			if idx == n:
				res.append("".join(comb))
				return

			for c in DAIL_ALPH[int(digits[idx])]:
				comb.append(c)
				findComb(idx + 1)
				comb.pop()

		findComb(0)
		return res


