class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        

        numMap = {}
        res = []
        target = math.floor(len(nums) / 3)

        for num in nums:
            if num not in numMap:
                numMap[num] = 0

            numMap[num] += 1

        for numPair in numMap.items():
            key, val = numPair

            if val > target:
                res.append(key)


        return res
        