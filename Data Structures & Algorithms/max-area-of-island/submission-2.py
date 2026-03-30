class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        biggest = 0

        def dfs(r, c):
            # Check boundaries and water immediately
         
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            size = 1
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                size += dfs(r + dr, c + dc)

            return size

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    current_size = dfs(i,j)
                    biggest = max(biggest, current_size)

        return biggest


