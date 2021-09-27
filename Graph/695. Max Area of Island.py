695. Max Area of Island

# BFS
import copy,collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    	if not grid: return 0
    	ocean = copy.deepcopy(grid)
    	rows = len(ocean)
    	columns = len(ocean[0])
    	directions = [(1,0),(0,1),(-1,0),(0,-1)]

    	helper_queue = collections.deque()

    	def validCheck(grid_,row,col):
    		nonlocal rows, columns
    		return 0<=row<rows and 0<=col<columns and grid_[row][col] == 1

    	max_area = 0
    	for row in range(rows):
    		for col in range(columns):
    			area = 0
    			if ocean[row][col] == 1:
    				area = 1
    				helper_queue.append((row,col))
    				ocean[row][col] = 2
    				while helper_queue:
    					i, j = helper_queue.popleft()
    					for dx, dy in directions:
    						newR, newC = i+dx, j+dy
    						if validCheck(newR, newC):
    							area += 1
    							ocean[newR][newC] = 2
    							helper_queue.append((newR,newC))
    			max_area = max(max_area, area)
    	return max_area




