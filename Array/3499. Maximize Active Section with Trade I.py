3499. Maximize Active Section with Trade I


# We are looking for a substr looks like 00001110000, so there are four change position (considered the first and last 1s)
class Solution:
	def maxActiveSectionsAfterTrade(self, s: str) -> int:
		aug_s = '1' + s + '1'
		n = len(aug_s)
		change_position = []

		for i in range(1, n):
			# Find a change position
			if aug_s[i] != aug_s[i - 1]:
				change_position.append((i, aug_s[i]))

		# The start point must be 0
		m = len(change_position)
		window_length = 4
		origin_gain = sum([1 for c in s if c == '1'])
		res = origin_gain

		if m < 4:
			return res

		for left in range(0, m, 2):
			right = left + window_length - 1
			if right >= m:
				break

			extra_gain = change_position[right][0] - change_position[left][0] - (change_position[right - 1][0] - change_position[left + 1][0])

			res = max(res, origin_gain + extra_gain)

		return res





