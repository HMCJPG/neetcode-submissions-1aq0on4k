class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        res = []

        zeroes = 0
        marker = 0

        for i, num in enumerate(nums):
            if num == 0:
                zeroes += 1
                marker = i

        if zeroes >= 2:
            return [0] * len(nums)

        elif zeroes == 1:
            res = [0] * len(nums)
            product = 1
            for i, num in enumerate(nums):
                if i != marker:
                    product *= num
            res[marker] = product

            return res

        else:
            master_product = 1
            for num in nums:
                master_product *= num

            res = [master_product] * len(nums)
            for i, num in enumerate(nums):
                res[i] = int(master_product / num)

            return res

        

