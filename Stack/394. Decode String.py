394. Decode String



class Solution:
	def decodeString(self, s: str) -> str:
		n = len(s)
		stack = deque()

		i = n - 1
		while i >= 0:
			c = s[i]

			if c == '[':
				# Star poping the substring
				substr = []
				while True:
					cur_char = stack.popleft()
					if cur_char == ']':
						break
					substr.append(cur_char)

				# Find the k
				k = deque()
				while i - 1 >= 0 and '0' <= s[i - 1] <= '9':
					k.appendleft(s[i - 1])
					i -= 1

				# decoding
				decode_substr = int(''.join(k)) * ''.join(substr)
				stack.appendleft(decode_substr)

			else:
				stack.appendleft(c)
			
			i -= 1

		return ''.join(stack)

