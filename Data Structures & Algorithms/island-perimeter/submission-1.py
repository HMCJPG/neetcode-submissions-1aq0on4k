class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        

        rows, cols = len(grid), len(grid[0])
        seen = set()

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    seen.add((r,c))

        perimeter = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    perimeter += 4

                    if (r + 1, c) in seen:
                        perimeter -= 1
                    if (r - 1, c) in seen:
                        perimeter -= 1
                    if (r, c + 1) in seen:
                        perimeter -= 1
                    if (r, c - 1) in seen:
                        perimeter -= 1

        return perimeter
                    


        
