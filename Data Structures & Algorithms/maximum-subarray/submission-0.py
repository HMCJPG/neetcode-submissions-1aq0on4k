class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        global_max = nums[0]
        local_max = nums[0]

        for i in range(1, len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(local_max, global_max)

        return global_max