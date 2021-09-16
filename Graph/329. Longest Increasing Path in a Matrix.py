329. Longest Increasing Path in a Matrix


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


# 方法二：拓扑排序