class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows, cols = len(grid), len(grid[0])
        maximal = 0


        def dfs(i,j):

            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            size = 1
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                size += dfs(i + dr, j + dc)

            return size





        for r in range(rows):
            for c in range(cols):
                current_max = dfs(r,c)
                maximal = max(current_max, maximal)

        return maximal