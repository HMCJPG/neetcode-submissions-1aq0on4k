class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        max_area = 0

        m,n = len(grid), len(grid[0])
        

        def dfs(i: int, j: int):

            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            area = 1

            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)

            return area


        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area
















