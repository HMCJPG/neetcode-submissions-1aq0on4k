class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):

            dirs = [(1,0), (-1,0), (0,1), (0,-1)]

            for dir in dirs:
                dr, dc = dir
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    dfs(nr, nc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i,j)

        return islands


        