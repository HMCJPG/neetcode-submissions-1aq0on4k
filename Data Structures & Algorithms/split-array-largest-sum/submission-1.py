class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left, right = max(nums), sum(nums)
        best = right

        while left <= right:
            mid = (left + right) // 2

            if self.isValid(nums, k, mid):
                best = mid
                right = mid - 1

            else:
                left = mid + 1

        return best


    def isValid(self, nums, k, maxSize) -> bool:
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