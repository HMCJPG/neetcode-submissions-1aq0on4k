class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {}

        for word in words:
            for c in word:
                adj[c] = set()

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    c1, c2 = w1[j], w2[j]
                    adj[c1].add(c2)
                    break

        res = []
        visit = {}

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)
            return False

        for c in adj:
            if dfs(c):
                return ""

        return "".join(res[::-1])












