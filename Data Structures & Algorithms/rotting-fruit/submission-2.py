from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        dirs = [(1,0),(-1,0),(0,1), (0,-1)]

        fresh = 0
        minutes = 0

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j, minutes))

        while queue:
            r,c, minute = queue.popleft()

            minutes = max(minutes, minute)

            for x, y in dirs:
                nr, nc = r + x, c + y

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, minutes + 1))
                    fresh -= 1


        if fresh == 0:
            return minutes
        else:
            return -1








