1431. Kids With the Greatest Number of Candies


class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		max_candies = max(candies)
		n = len(candies)
		res = []

		for i in range(n):
			if candies[i] + extraCandies >= max_candies:
				res.append(True)
			else:
				res.append(False)

		return res