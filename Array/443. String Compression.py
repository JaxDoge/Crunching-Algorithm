443. String Compression

# Two pointers
# pr = pw = 0
# Need a counter to count the character appearance
# chars[pr + 1] != chars[pr] means we encounter a new character. Then we use pw to write current group result 

class Solution:
	def compress(self, chars: List[str]) -> int:

		n = len(chars)

		pr = pw = 0

		counter = 0

		while pr < n:
			cur_char = chars[pr]

			counter += 1

			# Check if it is the end of the group
			if pr + 1 >= n or chars[pr + 1] != cur_char:
				# write the character
				chars[pw] = cur_char
				pw += 1

				# write the appearance number if needed
				if counter > 1:
					cnt_list = list(str(counter))
					for i in range(len(cnt_list)):
						chars[pw] = cnt_list[i]
						pw += 1

				# reset the counter
				counter = 0

			# move pr ahead
			pr += 1

		return pw
