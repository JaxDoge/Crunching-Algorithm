1456. Maximum Number of Vowels in a Substring of Given Length

# Sliding window

class Solution:
	def maxVowels(self, s: str, k: int) -> int:
		vowels = {"a", "e", "i", "o", "u"}
		n = len(s)

		p1 = p2 = 0
		answer = 0

		# initialize the window
		for _ in range(k):
			if s[p2] in vowels:
				answer += 1
			p2 += 1
			# Note that p2 will be outbounded after this loop
		
		tmp_answer = answer
		# Move the window
		while p2 < n:
			# Move p1 will remove the first character
			if s[p1] in vowels:
				tmp_answer -= 1
			p1 += 1

			# Move p2 will add a new character
			if s[p2] in vowels:
				tmp_answer += 1
			p2 += 1

			# store the maximum answer
			answer = max(answer, tmp_answer)

		return answer
