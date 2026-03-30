class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            current = nums[middle]

            if current == target:
                return middle

            elif current < target:
                left = middle + 1

            else:
                right = middle - 1

        return -1