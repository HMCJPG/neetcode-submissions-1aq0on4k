class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []

        def backtrack(index, path):
            
            res.append(path[:])

            for i in range(index, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])

        return res

