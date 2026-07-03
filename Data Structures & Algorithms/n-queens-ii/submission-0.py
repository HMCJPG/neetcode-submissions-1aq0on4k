class Solution:
    def totalNQueens(self, n: int) -> int:
        
        cols = [False] * n
        posDiag = [False] * (2 * n - 1)
        negDiag = [False] * (2 * n - 1)
        count = 0

        def backtrack(r: int):
            nonlocal count

            if r == n:
                count += 1
                return
            
            for c in range(n):

                if cols[c] or posDiag[r + c] or negDiag[r - c + n - 1]:
                    continue

                cols[c] = True
                posDiag[r + c] = True
                negDiag[r - c + n -1] = True

                backtrack(r + 1)

                cols[c] = False
                posDiag[r + c] = False
                negDiag[r - c + n -1] = False


        backtrack(0)

        return count



        