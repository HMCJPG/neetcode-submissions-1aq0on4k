class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        left, right = 0, len(nums) - 1
        hit = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                hit = mid
                break
            
            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1


        if hit == -1:
            return [-1,-1]

        else:
            leftPointer = hit
            rightPointer = hit

            while leftPointer >= 0 and nums[leftPointer] == target:
                leftPointer -= 1

            while rightPointer < len(nums) and nums[rightPointer] == target:
                rightPointer += 1

        return [leftPointer + 1, rightPointer - 1]








