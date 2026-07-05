from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for (a,b), val in zip (equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))


        def bfs(src: str, dst: str) -> float:

            if src not in graph or dst not in graph:
                return -1.0

            q = deque([(src, 1.0)])
            visited = {src}

            while q:
                node, prod = q.popleft()
                if node == dst:
                    return prod

                for nei, weight, in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, prod * weight))

            return -1.0

        return [bfs(a,b) for a,b in queries]







