54. Spiral Matrix


class Solution:
    def __init__(self):
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        res = []
        total_len = rows * cols

        self.move(matrix, rows, cols, total_len, 0, 0, 0, res)
        return res


    def move(self, matrix, rows, cols, total_len, dir, i, j, res):
        if len(res) == total_len:
            return


        res.append(matrix[i][j])
        matrix[i][j] = '*'

        #  determine next move
        new_i = i + self.directions[dir][0]
        new_j = j + self.directions[dir][1]

        if new_i >= rows or new_j >= cols or matrix[new_i][new_j] == '*':
            # not a valid direction, change it
            dir = (dir + 1) % 4
            new_i = i + self.directions[dir][0]
            new_j = j + self.directions[dir][1]

        return self.move(matrix, rows, cols, total_len, dir, new_i, new_j, res)





