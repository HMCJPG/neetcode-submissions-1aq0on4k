class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        summed = sum(nums)

        if summed % 2 != 0:
            return False

        target = int(summed // 2)

        dp = [False] * summed
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        return dp[target]