93. Restore IP Addresses


# Backtrack
class Solution:
	def restoreIpAddresses(self, s: str) -> list[str]:
		n = len(s)
		res = []

		def backtrack(start, parts):
			remaining_chars = n - start
			remaining_parts = 4 - len(parts)

			# Each remaining part need 1~3 digits
			if not remaining_parts <= remaining_chars <= remaining_parts * 3:
				return

			# If no more part needed, no more character left
			# We find one solution
			if remaining_parts == 0:
				res.append('.'.join(parts))
				return

			for length in range(1, 4):
				end = start + length

				if end > n:
					break

				cand_part = s[start:end]
				if length > 1 and s[start] == '0':
					break
				
				if int(cand_part) > 255:
					break
				
				parts.append(cand_part)
				backtrack(end, parts)
				parts.pop()

		backtrack(0, [])
		return res