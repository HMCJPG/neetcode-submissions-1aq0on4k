class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []


        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited):
            visited.add((r,c))
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]

            for ur, uc in dirs:
                nr, nc = r + ur, c + uc

                if (0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]) and (nr,nc) not in visited:
                    dfs(nr, nc, visited)

        pacific = set()
        atlantic = set()

        for r in range(rows):
            dfs(r, 0, pacific)
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)


        result = list(map(list, pacific & atlantic))

        return result




        