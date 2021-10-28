174. Dungeon Game


# dp table
# 计算从 dp[i][j] 到 dp[-1][-1] 所需最小 hp, base case 是 dp[-1][-1]
# 反方向遍历矩阵
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    	rows = len(dungeon)
    	cols = len(dungeon[0])

    	dp = [[0 for _ in range(cols)] for _ in range(rows)]

    	dp[-1][-1] = (-1)*dungeon[-1][-1] + 1 if dungeon[-1][-1] < 0 else 1

    	for row in range(rows-1, -1, -1):
    		for col in range(cols-1, -1, -1):
    			if dp[row][col] != 0:
    				continue
    			if row == rows-1:
    				tmp = dp[row][col+1] - dungeon[row][col]
    			elif col == cols-1:
    				tmp = dp[row+1][col] - dungeon[row][col]
    			else:
    				tmp = min(dp[row+1][col], dp[row][col+1]) - dungeon[row][col]
    			dp[row][col] = tmp if tmp>0 else 1
        return dp[0][0]
