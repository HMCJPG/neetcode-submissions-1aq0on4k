class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if not nums:   
            return 0


        jumps = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest =  max(farthest, nums[i] + i)

            if i == end:
                jumps += 1
                end = farthest

        return jumps
            