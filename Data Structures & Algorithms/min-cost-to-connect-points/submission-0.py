class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):

                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        edges.sort()

        parent = list(range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i,j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        min_cost = 0
        edge_count = 0

        for cost, u, v in edges:
            if union(u,v):
                edge_count += 1
                min_cost += cost

                if edge_count == n - 1:
                    break

        return min_cost
            









