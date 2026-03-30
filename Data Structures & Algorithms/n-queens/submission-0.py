class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        path = []

        def backtrack(row, col_set, diag1, diag2, path):

            # We've found a valid board, convert it and sent it in
            if row == n:

                board = []

                for col in path:
                    row_str = ['.'] * n
                    row_str[col] = 'Q'
                    board.append(''.join(row_str))
                res.append(board)
                return

            for col in range(n):
                if col in col_set or (row - col) in diag1 or (row + col) in diag2:
                    continue

                col_set.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                path.append(col)
                
                backtrack(row + 1, col_set, diag1, diag2, path)

                path.pop()
                diag2.remove(row + col)
                diag1.remove(row - col)
                col_set.remove(col)


        backtrack(0, set(), set(), set(), [])
        return res









