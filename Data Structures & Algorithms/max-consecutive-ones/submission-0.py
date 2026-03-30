class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        globalMax = 0
        localMax = 0

        for num in nums:

            if num == 1:
                localMax += 1

            else:
                localMax = 0

            if localMax >= globalMax:
                globalMax = localMax

        return globalMax
        