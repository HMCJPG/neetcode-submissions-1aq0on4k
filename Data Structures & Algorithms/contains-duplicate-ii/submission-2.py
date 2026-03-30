class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        holding = set()

        for i in range(len(nums)):

            if holding and nums[i] in holding:
                return True

            holding.add(nums[i])
            if i >= k:
                holding.remove(nums[i - k])


        return False


