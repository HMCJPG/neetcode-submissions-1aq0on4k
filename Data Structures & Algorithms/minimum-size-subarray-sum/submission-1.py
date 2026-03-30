class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        total = 0
        start = 0
        minSize = 0
        globalMin = float('inf')
        

        for i in range(len(nums)):

            total += nums[i]

            while total >= target:

                minSize = i - start + 1

                total -= nums[start]
                start += 1
                globalMin = min(globalMin, minSize)


        return min(globalMin, minSize)