class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False

        if self.rank[rootA] < self.rank[rootB]:
            rootA, rootB = rootB, rootA

        self.parent[rootB] = rootA
        if self.rank[rootA] == self.rank[rootB]:
            self.rank[rootA] += 1

        self.components -= 1
        return True


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if any(x == 1 for x in nums):
            return False

        max_num = max(nums)

        spf = list(range(max_num + 1))
        for i in range(2, int(max_num ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i



        def prime_factors(x:int):
            factors = []
            while x > 1:
                p = spf[x]
                factors.append(p)
                while x % p == 0:
                    x //= p
            return factors


        uf = UnionFind(n)
        owner = {}

        for i, num in enumerate(nums):
            for p in set(prime_factors(num)):
                if p in owner:
                    uf.union(i, owner[p])
                else:
                    owner[p] = i

        root = uf.find(0)
        for i in range(1, n):
            if uf.find(i) != root:
                return False
        return True
        
        


