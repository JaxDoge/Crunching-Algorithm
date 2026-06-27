1207. Unique Number of Occurrences



class Solution:
	def uniqueOccurrences(self, arr: List[int]) -> bool:
		occur_map = defaultdict(int)
		for i in range(len(arr)):
			occur_map[arr[i]] += 1

		freq_map = defaultdict(bool)

		for num, freq in occur_map.items():

			if freq_map[freq]:
				return False

			freq_map[freq] = True

		return True

