1291. Sequential Digits

# @cache cannot work with prefix: List[int]. Lists are unhashable.

class Solution:
	def sequentialDigits(self, low: int, high: int) -> List[int]:
		def solve(num: int) -> List[int]:
			digits = str(num)
			n = len(digits)
			res = []

			def intListToNumber(numbers: List[int]):
				ans = 0
				for num in numbers:
					ans = ans * 10 + num
				return ans

			def dfs(pos, prefix: List[int], started, tight):
				if pos == n:
					res.append(intListToNumber(prefix))
					return

				limit = int(digits[pos]) if tight else 9

				for d in range(limit + 1):
					next_tight = tight and d == limit
					# If still padding leading zero
					if not started and d == 0:
						prefix.append(d)
						dfs(pos + 1, prefix, started, next_tight)
					# If the construction not starts, we can try non-zero digit
					elif not started:
						prefix.append(d)
						dfs(pos + 1, prefix, True, next_tight)
					else:
						pre_digit = prefix[-1] # prefix should be non-empty
						# If we cannot continue constructing or d is invalid
						if pre_digit == 9 or pre_digit != d - 1:
							continue
						# d is valid
						else:
							prefix.append(d)
							dfs(pos + 1, prefix, started, next_tight)

					prefix.pop()

			dfs(0, [], False, True)
			return res

		return [x for x in solve(high) if x >= low]


# Sequential-digit numbers can only be substrings of: 123456789
# Simple sliding windows
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        ans = []

        for length in range(2, 10):
            for start in range(10 - length):
                num = int(digits[start:start + length])

                if low <= num <= high:
                    ans.append(num)

        return ans

