3517. Smallest Palindromic Rearrangement I

# Note the central character should be the same if the length is odd
class Solution:
	def smallestPalindrome(self, s: str) -> str:
		n = len(s)
		if n < 2:
			return s
			
		res_list = deque()
		s_list = []

		if n % 2 != 0:
			res_list.append(s[n // 2])
			s_list = list(s[:n // 2]) + list(s[n // 2 + 1:])
		else:
			s_list = list(s)

		s_list.sort(reverse = True)

		i = 0
		while i < n - 1:
			res_list.appendleft(s_list[i])
			res_list.append(s_list[i + 1])
			i += 2

		return "".join(res_list)


# Note the characters are a-z
# Bin count sort

class Solution:
	def smallestPalindrome(self, s: str) -> str:
		n = len(s)
		mid_idx = n // 2

		bucket = [0] * 26

		for i in range(mid_idx):
			bucket[ord(s[i]) - ord('a')] += 1

		left = [chr(i + ord('a')) * bucket[i] for i in range(26) if bucket[i] > 0]
		mid = [s[mid_idx]] if n % 2 != 0 else []
		right = left[::-1]

		return "".join(left + mid + right)