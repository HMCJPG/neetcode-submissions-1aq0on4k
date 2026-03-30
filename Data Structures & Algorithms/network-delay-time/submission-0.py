from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v, t))

        
        heap = [(0,k)]
        dist = {}
        

        while heap:
            t, node = heapq.heappop(heap)

            if node in dist:
                continue
            dist[node] = t

            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (t + w, nei))

        if len(dist) < n:
            return -1

        else:
            return max(dist.values())















