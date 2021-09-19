130. Surrounded Regions
[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# DFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return

        rows, columns = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfsSearch(row, col):
            nonlocal board
            # 坐标非法，或者该坐标值不为'O'
            if not 0<=row<rows or not 0<=col<columns or board[row][col] != 'O':
                return

            board[row][col] = '#'  # Mark all node that connet to the edges
            for dx, dy in directions:
                newR, newC = row+dx, col+dy
                dfsSearch(newR, newC)

        # Iterate four edges
        for i in range(rows):
            dfsSearch(i,0)
            dfsSearch(i,columns-1)

        for i in range(1,columns-1):
            dfsSearch(0,i)
            dfsSearch(rows-1,i)

        # Iterate the whole board
        for row in range(rows):
            for col in range(columns):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == '#':
                    board[row][col] = 'O'

# BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        rows, columns = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # BFS queue
        import collections
        helper_queue = collections.deque()

        # BFS four edges
        for i in range(rows):
            if board[i][0] == 'O':
                helper_queue.append((i,0))
                board[i][0] = '#'
            if board[i][columns-1]:
                helper_queue.append((i,columns-1))
                board[i][columns-1] = '#'
        for i in range(1,columns):
            if board[0][i] == 'O':
                helper_queue.append((0,i))
                board[0][i] = '#'
            if board[rows-1][i] == 'O':
                helper_queue.append((rows-1,i))
                board[rows-1][i] = '#'

        # BFS inner cells
        while helper_queue:
            row, col = helper_queue.popleft()
            for dx, dy in directions:
                newR, newC = row+dx, col+dy
                if 0<=newR<rows and 0<=newC<columns and board[newR][newC] == 'O':
                    board[newR][newC] = '#'
                    helper_queue.append((newR,newC))

        for row in range(rows):
            for col in range(columns):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == '#':
                    board[row][col] = 'O'




# Union-Find Solution
class UF:
    def __init__(self, count: int):
        self.count = count
        self.parent = [i for i in range(self.count)]
        self.size = [1] * self.count

    # Return the root node of the node
    def find(self, node: int) -> int:
        while node != self.parent[node]:
            # compress tree
            self.parent[node] = self.parent[self.parent[node]]
            # move upper
            node = self.parent[node]
        return node

    # Union two trees
    def union(self,p,q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq: return

        if self.size[rootp] >= self.size[rootq]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]

        self.count -= 1

    def connected(self,p,q) -> bool:
        rootp = self.find(p)
        rootq = self.find(q)
        return rootp == rootq从·


# 二维坐标 (x,y) 可以转换成 x * n + y 这个数（m 是棋盘的行数，n 是棋盘的列数 
# 这是将二维坐标映射到一维的常用技巧。

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not list or not list[0]: return
        
        rows = len(board)
        columns = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # Union-Find Class, save a position for the dummy root
        helper_uf = UF(rows * columns + 1)
        dummy = rows * columns

        # 将首列和末列的 O 与 dummy 连通
        for i in range(rows):
            if board[i][0] == 'O':
                helper_uf.union(dummy, i*columns + 0)
            if board[i][columns-1] == 'O':
                helper_uf.union(dummy, i*columns + columns -1)

        # 将首行和末行的 O 与 dummy 连通
        for i in range(columns):
            if board[0][i] == 'O':
                helper_uf.union(dummy, i) 
            if board[rows-1][i] == 'O':
                helper_uf.union(dummy,(rows-1)*columns+i)

        # 遍历矩阵中间 0 节点，寻找和 dummy 树相邻的 0 节点加入 dummy 树
        for row in range(1,rows-1):
            for column in range(1,columns-1):
                if board[row][column] == 'O':
                    # 将这个节点和相邻的 0 节点 union 
                    for dx,dy in directions:
                        newR, newC = row+dx, column+dy
                        if board[newR][newC] == 'O':
                            helper_uf.union(row*columns + column, newR*columns + newC)

        # 替换所有不和 dummy 联通的节点
        for row in range(1,rows-1):
            for column in range(1,columns-1):
                if not helper_uf.connected(row*columns+column,dummy):
                    board[row][column] = 'X'







        
