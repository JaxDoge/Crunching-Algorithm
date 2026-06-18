151. Reverse Words in a String

from collections import deque

class Solution:
	def reverseWords(self, s: str) -> str:
		
		n = len(s)
		ps = 0
		pe = n - 1

		# remove the leading and trailing space
		while True:
			if ps > pe:
				break
			if s[ps] == " ":
				ps += 1
			if s[pe] == " ":
				pe -= 1

			if s[ps] != " " and s[pe] != " ":
				break

		res_stack = deque()

		i = j = ps

		while True:
			# move j to the nearest space
			while j <= pe and s[j] != " " :
				j += 1

			# add the word to the stack
			res_stack.appendleft(s[i:j])


			# check if j is outbounded
			if j > pe:
				break

			# move j to next word start
			while s[j] == " ":
				j += 1

			i = j

		return " ".join(res_stack)




# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?