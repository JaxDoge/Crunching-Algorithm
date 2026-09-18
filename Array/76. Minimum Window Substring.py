76. Minimum Window Substring


# 滑动窗口
# 右指针移动寻找可行解，左指针移动优化当前可行解，优化完更新目前最优解，直到 right 移动到尽头
from collections import Counter

class Solution:
	def minWindow(self, s: str, t: str) -> str:
		if not t or len(t) > len(s):
			return ""

		need = Counter(t)
		missing = len(t)
		left = 0
		best_start = 0
		best_len = float("inf")

		for right, char in enumerate(s):
			if need[char] > 0:
				missing -= 1
			need[char] -= 1

			while missing == 0:
				window_len = right - left + 1
				if window_len < best_len:
					best_start = left
					best_len = window_len

				# Remove the leftmost character.
				left_char = s[left]
				need[left_char] += 1
				if need[left_char] > 0:
					missing += 1
				left += 1

		return "" if best_len == float("inf") else s[best_start:best_start + best_len]