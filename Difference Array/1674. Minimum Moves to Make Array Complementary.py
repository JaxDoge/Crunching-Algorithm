1674. Minimum Moves to Make Array Complementary

# Note that the possible target sum are 2 ... 2 * limit
# And for any pair (a, b), their original sum is also between 2 ... 2 * limit
# So the basic idea is that we need to check each possible target and calculate the moves
# We can assume any target needs 0 move initially [0, 0, ... ,0]
# For a given pair (a, b), how would it affect the array above? Range Update!
# S < low + 1             → 2 moves
# low + 1 <= S < cur      → 1 move
# S == cur                → 0 moves
# cur < S <= high + limit → 1 move
# S > high + limit        → 2 moves
# moves
#   2 ───────┐                 ┌──────
#            │                 │
#   1        └────────┐ ┌──────┘
#                     │ │
#   0                 └─┘
#                     cur

#       low+1                 high+limit

# Here is difference array kicks in. And we can record the minimum move on the fly

class Solution:
	def minMoves(self, nums: List[int], limit: int) -> int:
		# We only need [2, ... , 2*limit], but the extra index can help us simplify the diff-array update
		diff = [0] * (2 * limit + 2)

		n = len(nums)

		for i in range(n // 2):
			a = nums[i]
			b = nums[n - 1 - i]

			high = max(a, b)
			low = min(a, b)
			cur = a + b

			diff[2] += 2
			diff[low + 1] -= 1
			diff[cur] -= 1
			diff[cur + 1] += 1
			diff[high + limit + 1] += 1

		res = float('inf')
		move = 0

		# Note we never touch diff[2 * limit + 1]
		for target in range(2, 2 * limit + 1):
			move += diff[target]
			res = min(res, move)

		return res

