class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        res = []

        def backtrack(start, path):
            if path not in res:
                res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])

        cleaned = []
        for r in res:
            if sorted(r) not in cleaned:
                cleaned.append(sorted(r))

        return cleaned