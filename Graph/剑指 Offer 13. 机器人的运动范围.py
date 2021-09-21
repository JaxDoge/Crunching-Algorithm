剑指 Offer 13. 机器人的运动范围

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
    	res = 0
    	# 先找出所有不能去的cell
    	# 构建矩阵
    	grid = [[0 for _ in range(n)] for _ in range(m)]

    	for row in range(m):
    		for col in range(n):
    			if row <= 9:
    				digit_1 = 0
    				digit_2 = row
    			else:
    				digit_1 = row // 10
    				digit_2 = row % 10

    			if col <= 9:
    				digit_3 = 0
    				digit_4 = col
    			else:
    				digit_3 = col // 10
    				digit_4 = col % 10

    		    if digit_1 + digit_2 + digit_3 + digit_4 <= k:
    		    	grid[row][col] = 1
    		    else:
    		    	grid[row][col] = 0

        def validCheck(grid,row,col):
        	nonlocal m,n
        	return 0<=row<m and 0<=col<n and grid[row][col] == 1

        def dfsSearch(row, col):
        	nonlocal grid, res
        	if not validCheck(grid, row, col):
        		return
        		
			grid[row][col] = 2 # searched mark
        	res += 1
        	dfsSearch(row+1,col)
        	dfsSearch(row-1,col)
        	dfsSearch(row,col+1)
        	dfsSearch(row,col-1)

        dfsSearch(0,0)
        return res



