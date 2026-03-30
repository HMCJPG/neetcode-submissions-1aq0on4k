class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red = 0
        white = 0
        blue = 0

        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1

        index = 0

        while index < red:
            nums[index] = 0
            index += 1
        
        white += red


        while index < white:
            nums[index] = 1
            index += 1

        blue += white

        while index < blue:
            nums[index] = 2
            index += 1

        return nums
        