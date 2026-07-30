import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows, cols = len(heights), len(heights[0])
        minHeap = [(0,0,0)]
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]


        while minHeap:
            effort, r, c = heapq.heappop(minHeap)

            if (r,c) in visited:
                continue
            visited.add((r,c))

            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    nextEffort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(minHeap, (nextEffort, nr, nc))


        return 0