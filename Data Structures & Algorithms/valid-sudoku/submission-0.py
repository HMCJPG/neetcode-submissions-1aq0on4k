class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for val in row:
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # Check 3x3 boxes
        for boxRow in range(3):
            for boxCol in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[boxRow*3 + i][boxCol*3 + j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return True
