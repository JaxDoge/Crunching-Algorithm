59. Spiral Matrix II



class Solution:
    def __init__(self):
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.matrix = []

    def move(self, n, cur_num, dir, i, j):
        # base case
        if cur_num > n * n:
            return

        self.matrix[i][j] = cur_num

        new_i = i + self.directions[dir][0]
        new_j = j + self.directions[dir][1]

        if new_i >= n or new_j >= n or self.matrix[new_i][new_j] != '*':
            dir = (dir + 1) % 4
            new_i = i + self.directions[dir][0]
            new_j = j + self.directions[dir][1]

        return self.move(n, cur_num + 1, dir, new_i, new_j)

    def generateMatrix(self, n: int) -> List[List[int]]:
        self.matrix = [['*'] * n for _ in range(n)]

        self.move(n, 1, 0, 0, 0)

        return self.matrix
