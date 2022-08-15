348. Design Tic-Tac-Toe



# Naive Solution
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.step = 0

    def checkDiag(self):
        diag1 = self.board[0][0]
        diag2 = self.board[self.n-1][0]
        for i in range(1, self.n):
            if self.board[i][i] == 0:
                diag1 = 0 
            if self.board[self.n - 1 - i][i] == 0:
                diag2 = 0
            if self.board[i][i] != diag1:
                diag1 = 0 
            if self.board[self.n - 1 - i][i] != diag2:
                diag2 = 0 

        return diag1 if diag1 != 0 else diag2

    def move(self, row: int, col: int, player: int) -> int:
        self.step += 1
        self.board[row][col] = player

        # check column
        colPawn = player
        for i in range(self.n):
            if self.board[i][col] != player:
                colPawn = 0 

        if colPawn != 0:
            return player

        # check row
        rowPawn = player
        for j in range(self.n):
            if self.board[row][j] != player:
                rowPawn = 0

        if rowPawn != 0:
            return rowPawn

        # check diagonals if necessay
        if row == col or row + col == self.n - 1:
            if self.checkDiag() != 0:
                return self.checkDiag()

        # no winner
        return 0




# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)