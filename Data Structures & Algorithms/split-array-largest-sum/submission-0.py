class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        low = max(nums)
        high = sum(nums)
        best = high

        while low <= high:
            mid = (low + high) // 2

            if self.canSplit(nums, k, mid):
                best = mid
                high = mid -1
            else:
                low = mid + 1

        return best
        



    def canSplit(self, nums, k, maxSize) -> bool:
        cases = 1
        current = 0

        for num in nums:
            if current + num > maxSize:
                cases += 1
                current = num

            else:
                current += num

        if cases > k:
            return False
        else:
            return True