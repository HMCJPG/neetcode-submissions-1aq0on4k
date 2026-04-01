class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = {}
        self.cols = {}

        self.diag = 0
        self.anti_diag = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        val = 1 if player == 1 else -1

        self.rows[row] = self.rows.get(row, 0) + val
        self.cols[col] = self.cols.get(col, 0) + val

        if row == col:
            self.diag += val

        if row + col == self.n - 1:
            self.anti_diag += val

        if (abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.anti_diag) == self.n):
            return player

        return 0

        

        




# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
