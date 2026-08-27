1502. Can Make Arithmetic Progression From Sequence


class Solution:
	def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
		n = len(arr)
		arr.sort()

		cali = arr[0] - arr[1]

		for i in range(1, n - 1):
			if arr[i] - arr[i + 1] != cali:
				return False

		return True

