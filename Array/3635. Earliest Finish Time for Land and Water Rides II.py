3635. Earliest Finish Time for Land and Water Rides II

# Brutal force can TLE

class Solution:
	def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
		n = len(landStartTime)
		m = len(waterStartTime)

		landInterval = []
		waterInterval = []

		for i in range(n):
			intrvl = [landStartTime[i], landStartTime[i] + landDuration[i]]
			landInterval.append(intrvl)

		for i in range(m):
			intrvl = [waterStartTime[i], waterStartTime[i] + waterDuration[i]]
			waterInterval.append(intrvl)

		res = float('inf')

		# Land first
		x = min([end for _, end in landInterval])
		for i in range(m):
			land_water = max(x, waterInterval[i][0]) + (waterInterval[i][1] - waterInterval[i][0])
			res = min(res, land_water)


		# Water first
		x = min([end for _, end in waterInterval])
		for i in range(n):
			water_land = max(x, landInterval[i][0]) + (landInterval[i][1] - landInterval[i][0])
			res = min(res, water_land)	

		return res	