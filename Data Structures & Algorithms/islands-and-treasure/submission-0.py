from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        if not grid:
            return 0

        m,n = len(grid), len(grid[0])

        INF = (2**31) - 1

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]


        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))

        
        while q:
            i,j = q.popleft()

            for x,y in dirs:
                ni, nj = i + x, j + y

                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == INF:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni,nj))

