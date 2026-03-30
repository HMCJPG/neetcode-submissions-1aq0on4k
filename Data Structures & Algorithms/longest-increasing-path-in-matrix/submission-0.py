class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])

        memo = [[0] * cols for i in range(rows)]

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r,c):

            if memo[r][c] != 0:
                return memo[r][c]

            best = 1

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > matrix[r][c]:
                        best = max(best, 1 + dfs(nr, nc))


            memo[r][c] = best
            return best

        
        ans = 0

        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i,j))

        return ans











