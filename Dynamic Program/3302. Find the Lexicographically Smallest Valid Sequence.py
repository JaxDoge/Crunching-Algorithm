3302. Find the Lexicographically Smallest Valid Sequence

# We need to match the character as early as possible to meed the Lexicographically Smallest requirement
# And we have one chance to use the mismatch
# Why can we greedily use a mismatch? Because the array right[j] tells us if right[j + 1] > i, there must be a exact match sequence later (still have room for that)
# Otherwise we should skip current word1[i] and save the mismatch later (imaging word[j+1] never appear in word1, we need to save the mismatch for it) 
class Solution:
	def validSequence(self, word1: str, word2: str) -> List[int]:
		n = len(word1)
		m = len(word2)

		if m > n:
			return []

		# Construct the right array which denote the last change (index) in word1 for word2[j:] to exactly match
		right = [-1] * m
		j = m - 1
		for i in range(n - 1, -1, -1):
			if j < 0:
				break
			elif word1[i] == word2[j]:
				right[j] = i
				j -= 1

		ans = []
		j = 0
		use_mismatch = False

		for i in range(n):
			if j == m:
				break

			# Best case
			if word1[i] == word2[j]:
				ans.append(i)
				j += 1
			# Otherwise try to use our one mismatch here. Note that if j == m - 1 we can just use the mismatch
			elif not use_mismatch and (j == m - 1 or right[j+1] > i):
				ans.append(i)
				use_mismatch = True
				j += 1

			
		return ans if j == m else []
