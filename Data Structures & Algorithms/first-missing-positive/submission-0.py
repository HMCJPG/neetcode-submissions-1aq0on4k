class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        minimal = 1
        seen = set()
        
        for num in nums:

            if num >= 0:
                seen.add(num)

        for i in range(len(seen)):
            if minimal in seen:
                minimal += 1
            else:
                break

        return minimal
