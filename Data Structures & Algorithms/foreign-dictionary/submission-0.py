class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # 1. Initialize Adjacency List
        # We need an entry for every unique letter found in any word.
        adj = {}
        for w in words:
            for c in w:
                if c not in adj:
                    adj[c] = set()

        # 2. Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # Edge Case: "apple" cannot come before "app"
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""
            
            # Find the first differing character
            for j in range(min_len):
                if w1[j] != w2[j]:
                    char1, char2 = w1[j], w2[j]
                    # This means char1 comes BEFORE char2
                    # So we draw an arrow char1 -> char2
                    adj[char1].add(char2)
                    break 
        
        # 3. DFS for Topological Sort
        visit = {} # False=visited, True=current path
        res = []
        
        def dfs(c):
            if c in visit:
                return visit[c] # Return True if cycle found, False if safe
            
            visit[c] = True # Mark as visiting (current path)
            
            for nei in adj[c]:
                if dfs(nei):
                    return True # Cycle detected
            
            visit[c] = False # Mark as fully visited
            res.append(c)
            return False
        
        # Run DFS on every node
        for c in adj:
            if dfs(c):
                return "" # Cycle found
                
        # Reverse to get the correct order (parents before children)
        return "".join(res[::-1])