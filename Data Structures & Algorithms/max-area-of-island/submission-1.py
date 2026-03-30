class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])

        globalMax = 0

        def dfs(i,j):

            
            # If out of bounds, or if we hit water, the connection dies
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0

            # We're in bounds and we're at land, so we want to check for more land
            area = 1
            grid[i][j] = 0
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    globalMax = max(area, globalMax)

        return globalMax
