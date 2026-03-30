class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not isinstance(nums, list):
            return -1


        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            midpoint = nums[mid]

            if midpoint == target:
                return mid
            elif midpoint < target:
                left = mid + 1
            elif midpoint > target:
                right = mid - 1

        return -1