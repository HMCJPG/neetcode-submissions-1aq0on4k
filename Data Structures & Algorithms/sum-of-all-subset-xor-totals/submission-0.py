class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        result = 0

        def backtrack(index, current_xor):

            nonlocal result
            result += current_xor

            for i in range(index, len(nums)):
                backtrack(i + 1, current_xor ^ nums[i])

        backtrack(0,0)

        return result