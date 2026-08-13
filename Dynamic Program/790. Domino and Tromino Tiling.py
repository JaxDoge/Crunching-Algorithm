790. Domino and Tromino Tiling

class Solution:
	def numTilings(self, n: int) -> int:
		MOD = 1e9 + 7

		if n <= 2:
			return n

		f = [0] * (n + 1)
		p = [0] * (n + 1)

		f[1] = 1
		f[2] = 2
		p[2] = 1

		# Note that the 2*p can happend in the p[i] calculation, which means we maintain the exact partial tilings number
		# Currently we only maintain the upper tile missing situation

		for i in range(3, n + 1):
			f[i] = (f[i-1] + f[i-2] + 2*p[i-1]) % MOD
			p[i] = (f[i-2] + p[i - 1]) % MOD

		return int(f[n])