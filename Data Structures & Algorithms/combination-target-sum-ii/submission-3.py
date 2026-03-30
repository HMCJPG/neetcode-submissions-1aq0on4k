class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        candidates.sort() 
        path = []
        res = []

        def backtrack(current_sum, start):

            if current_sum > target:
                return

            elif current_sum == target:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(current_sum + candidates[i], i + 1)
                path.pop()

        backtrack(0,0)

        return res
            