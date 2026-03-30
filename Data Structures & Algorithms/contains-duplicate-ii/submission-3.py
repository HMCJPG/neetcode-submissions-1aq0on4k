class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        holding = []

        for i in range(len(nums)):

            if holding and nums[i] in holding:
                return True

            holding.append(nums[i])
            if i >= k:
                holding.pop(0)


        return False


