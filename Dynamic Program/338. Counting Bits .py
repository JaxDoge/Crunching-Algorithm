338. Counting Bits

# For even number ne, the most insignificant binary digit muse be 0
# So the result is equal to ne >> 1
# For odd number no, the result is equal to no >> 1 + 1
class Solution:
	def countBits(self, n: int) -> List[int]:
		ans = [0]

		for i in range(1, n + 1):
			if i % 2 == 0:
				ans.append(ans[i >> 1])
			else:
				ans.append(ans[i >> 1] + 1)

		return ans