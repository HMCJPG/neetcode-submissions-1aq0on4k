class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums = sorted(nums)

        n = len(nums)
        currentLongest = 1
        totalLongest = 1

       # print(nums)
        for i in range(n-1):
            if nums[i+1] == nums[i]+1:
                currentLongest+=1
            elif nums[i+1] == nums[i]:
                continue
            else:
                totalLongest = max(totalLongest, currentLongest)
                currentLongest = 1

        totalLongest = max(totalLongest, currentLongest)
        return totalLongest