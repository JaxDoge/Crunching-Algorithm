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





「方法一」中使用了记忆化存储和深度优先搜索，这里的深度优先搜索可以替换成广度优先搜索吗？
可以，参考评论区Meg，和DFS一样需要一个MxN的数组来存放搜索结果，但结果存放顺序则与DFS相反，
也就是说： DFS中memo的每个节点存放的是从该节点到最长路径末端的距离。 
而BFS中每个节点存放的则是从起点到该节点的距离。BFS中由于路径起点是随机分布在矩阵内。
所以如果按矩阵顺序遍历，取节点作为起点计算得到的结果很可能只是某条长路径中的末端部分。
很显然，这样的结果没法重复使用实现减枝。所以需要在每次BFS遍历时，按节点值大小排序并记录索引，
然后按排序后节点索引进行遍历。这样凡是计算过的节点必然是正确的，不需要再进行计算。
（这样BFS的queue结构变成了PriorityQueue，也就是从BFS变成了A*搜索。）

「方法二」中基于拓扑排序对排序后的有向无环图DAG做了层次遍历，如果没有拓扑排序直接进行广度优先搜索会发生什么？
很大可能会返回一个不是最长的递增路径，如示例1，起始点是9，已经是最大值了，结果输出了0.

「方法二」中如果不使用拓扑排序，而是直接按照矩阵中元素的值从大到小进行排序，并依此顺序进行状态转移，那么可以得到正确的答案吗？如果是从小到大进行排序呢？
这个是可以的，只要有了排序，那么从最小的数值开始BFS，就能搜索到正确答案。不过2D数组的最快排序时间是O(MN)，和题解中的两个方法时间复杂度一致。

「变式」给定一个整数矩阵，找出符合以下条件的路径的数量：这个路径是严格递增的，且它的长度至少是 3。矩阵的边长最大为 10^3，答案对 10^9+7 取模。其他条件和题目相同。思考：是否可以借鉴这道题的方法？可以，但是如果使用memo+DFS的方法一，很可能会爆内存栈，因此只能使用方法二。这里有一个【长度至少是 3】的限制，很可能是一个优化的着手点，不过我没有用到，希望大家讨论更好的优化方法。