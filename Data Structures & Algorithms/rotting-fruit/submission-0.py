from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        fresh = 0
        minutes = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue:
            r,c,minute = queue.popleft()
            minutes = max(minutes, minute)

            for x, y in dirs:
                nr, nc = r + x, c + y

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2 # ROT THE FRUIT. IT'S ROTTEN!
                    fresh -= 1
                    queue.append((nr, nc, minute + 1))


        return minutes if fresh == 0 else -1













