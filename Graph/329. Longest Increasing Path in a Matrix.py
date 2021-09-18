329. Longest Increasing Path in a Matrix

# 这些方法本身应该都没有办法去记录路线本身，非常工程思维
# 方法一：记忆化深度优先搜索
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        # use lru_cache
        Directions = [(1,0),(-1,0),(0,1),(0,-1)]

        row_length = len(matrix[0])
        column_length = len(matrix)
        res = 0

        @lru_cache(maxsize = None)  # Python 自带递归 lru cache，复用重复计算结果
        def dfsTraverse(xaxis, yaxis):
            path_len = 1
            # 多叉树的 dfs，一共四个方向
            for x, y in Directions:
                new_xaxis = xaxis+x
                new_yaxis = yaxis+y
                # 判断移动路线是否合法，即是否移出矩阵边界，是否严格递增
                if 0 <= new_xaxis < row_length and 0 <= new_yaxis < column_length and matrix[yaxis][xaxis] < matrix[new_yaxis][new_xaxis]:
                    # Why use max()? Because there are four directions, which means multiple valid paths from this node, but there is only one best answer
                    path_len = max(path_len, dfsTraverse(new_xaxis,new_yaxis)+1)
            return path_len

        # Traver From Every Node
        for y in range(column_length):
            for x in range(row_length):
                res = max(res, dfsTraverse(x,y))
        return res


# 方法一：记忆化深度优先搜索 ，不用 lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        # use lru_cache
        Directions = [(1,0),(-1,0),(0,1),(0,-1)]

        row_length = len(matrix[0])
        column_length = len(matrix)
        res = 0
        # establish the memo
        memo = [[0 for _ in range(row_length)] for _ in range(column_length)]

        def dfsTraverse(xaxis, yaxis):
            nonlocal memo, matrix
            if memo[yaxis, xaxis]: return memo[yaxis, xaxis]
            path_len = 1
            # 多叉树的 dfs，一共四个方向
            for x, y in Directions:
                new_xaxis = xaxis+x
                new_yaxis = yaxis+y
                # 判断移动路线是否合法，即是否移出矩阵边界，是否严格递增
                # python 自动跳转到全局变量空间寻找 matrix
                if 0 <= new_xaxis < row_length and 0 <= new_yaxis < column_length and matrix[yaxis][xaxis] < matrix[new_yaxis][new_xaxis]:
                    path_len = max(path_len, dfsTraverse(new_xaxis,new_yaxis)+1)
            # record result in memo
            memo[yaxis, xaxis] = path_len
            return path_len

        # Traver From Every Node
        for y in range(column_length):
            for x in range(row_length):
                res = max(res, dfsTraverse(x,y))
        return res


# 方法二：逆向拓扑排序 + 广度优先, 从所有严格递增路线的最末尾开始寻找

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        # Bad Cases
        if not matrix:
            return res
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, columns = len(matrix), len(matrix[0])
        
        # BFS queue
        import collections
        helper_queue = collections.deque()
        
        # Initialize out-degree matrix
        out_degree = [[0] * columns for _ in range(rows)]        

        for i in range(rows):
            for j in range(columns):
                # calculate the out-degrees of every node
                for dx, dy in directions:
                    new_row = i + dx
                    new_column = j + dy
                    if 0<=new_row<rows and 0<=new_column<columns and matrix[i][j]<matrix[new_row][new_column]:
                        out_degree[i][j] += 1
                # 如果这个节点出度还是0，记录该节点进入广度搜索队列
                if out_degree[i][j] == 0:
                    helper_queue.append((i,j))
        
        # 类似层序遍历，需要子循环辅助先遍历完当前层
        while helper_queue:
            res += 1
            subsize = len(helper_queue)
            for _ in range(subsize):
                row, column = helper_queue.popleft()
                # 相邻节点出度 -1
                for dx, dy in directions:
                    new_row, new_column = row + dx, column + dy
                    # 有个疑问，最后一个判断条件需要吗？必须要，否则不是相邻节点了，会把其他路线提前截断
                    if 0<=new_row<rows and 0<=new_column<columns and matrix[row][column]>matrix[new_row][new_column]:
                        # 调整对应的 out_degree 节点中的出度值
                        out_degree[new_row][new_column] -= 1
                        # 如果该相邻节点已经是出度为 0，加入 queue
                        if out_degree[new_row][new_column] == 0:
                            helper_queue.append((new_row, new_column))

        return res





        