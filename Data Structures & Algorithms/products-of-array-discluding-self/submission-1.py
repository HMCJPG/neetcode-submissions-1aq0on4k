class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zeroCount = 0
        firstZero = 0


        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
                firstZero = i
            product = product * nums[i]

        if zeroCount >= 2:
            return [0]*len(nums)

        elif zeroCount == 1:
            product = 1
            for i in range(len(nums)):
                if i == firstZero:
                    continue
                product = product * nums[i]
            returnList = [0]*len(nums)
            returnList[firstZero] = product
            return returnList
        

        else:
            for i in range(len(nums)):
                holder = nums[i]
                nums[i] = int(product/holder)
            return nums            