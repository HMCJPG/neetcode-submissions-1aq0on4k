class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        graph = [[] for i in range(n)]

        for edge in edges:
            a,b = edge

            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                elif neighbor in visited:
                    return False
                elif not dfs(neighbor, node):
                    return False
            return True

        dfs(0, -1)

        return len(visited) == n


        return True