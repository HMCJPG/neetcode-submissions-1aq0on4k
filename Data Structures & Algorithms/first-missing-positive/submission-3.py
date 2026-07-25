class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        minimal = 1
        nums = set(nums)
        
        for i in range(len(nums)):

            if minimal in nums:
                minimal += 1
            else:
                break

        return minimal
