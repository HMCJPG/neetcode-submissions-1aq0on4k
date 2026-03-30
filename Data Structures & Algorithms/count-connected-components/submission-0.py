class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for i in range(n)]

        for edge in edges:
            a,b = edge

            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)


            
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count