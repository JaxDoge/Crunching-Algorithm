514. Freedom Trail

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        import collections
    	m = len(ring)
    	n = len(key)
    	memo = [[0 for _ in range(n)] for _ in range(m)]

        # Record the indices of every character, one character could appear in different positions
        char_to_index = collections.defaultdict(list)
        for i in range(m):
            char_to_index[ring[i]].append(i)

        def dp(i,j):
        	nonlocal ring, key, m, n, memo, char_to_index
        	if j == len(key):
        		return 0
            if memo[i][j] != 0:
                return memo[i][j]

            res = float('inf')
            for ind in char_to_index[key[j]]:
                # anticlockwise or clockwise rotate the ring
                steps = abs(ind - i)
                steps = min(steps, m - steps) + 1  # press button

                # dfs
                next_steps = dp(ind, j+1)
                res = min(res, steps+next_steps)

            memo[i][j] = res
            return memo[i][j]

        return dp(0,0)

