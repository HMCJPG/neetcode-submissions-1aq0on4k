class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = [i for i in range(n + 1)]


        def find(x):

            while x!= parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            pu, pv = find(u), find(v)

            if pu == pv:
                return [u, v]
            
            parent[pv] = pu