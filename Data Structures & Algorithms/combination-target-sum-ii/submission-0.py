from collections import defaultdict

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        res = []
        def backtrack(start, path, total):
            
            if total == target:
                res.append(path[:])
                return
            elif total > target:
                return
                
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)

        cleaned = []
        for r in res:
            solution = sorted(tuple(r))
            if solution not in cleaned:
                cleaned.append(solution)


        return [clean for clean in cleaned]