749. Contain Virus


# BFS + simulation
# Note that the frontiers and perimeters are not interchangable
# Because one inaffected frontier cell may have multiple perimeters (encompass)
class Solution:
	def containVirus(self, isInfected: List[List[int]]) -> int:
		rows, cols = len(isInfected), len(isInfected[0])

		def neighbors(r, c):
			for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
				if 0<=nr<rows and 0<=nc<cols:
					yield nr, nc

		def dfs(r, c):
			if (r, c) not in seen:
				seen.add((r, c))
				regions[-1].add((r, c))
				for nr, nc in neighbors(r, c):
					if isInfected[nr][nc] == 1:
						dfs(nr, nc)
					elif isInfected[nr][nc] == 0:
						# mark the frontier and perimeters needed.
						frontiers[-1].add((nr, nc))
						perimeters[-1] += 1

		res = 0

		while True:
			seen = set()
			regions = []
			frontiers = []
			perimeters = []

			for r in range(rows):
				for c in range(cols):
					if isInfected[r][c] == 1 and (r, c) not in seen:
						# We touch a new infected region
						regions.append(set())
						frontiers.append(set())
						perimeters.append(0)
						dfs(r, c)

			# We build the wall to quarantine the virus
			# So we can mark the region is clean
			# If there is one alive region left, it will still be picked up and mark clean (frontier length is 0)
			# So the exist condition is no region after scan
			if not regions:
				break

			# Quarantine the region threatening the most cells.
			quarantine_index = max(
				range(len(frontiers)),
				key=lambda i: len(frontiers[i])
			)

			res += perimeters[quarantine_index]

			# clean the quarantined area
			for r, c in regions[quarantine_index]:
				isInfected[r][c] = -1

			# Spread the infection
			for i, frontier in enumerate(frontiers):
				if i == quarantine_index:
					continue

				for r, c in frontier:
					isInfected[r][c] = 1

		return res



