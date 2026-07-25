from collections import defaultdict

from types import resolve_bases
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numMap = {}
        res = []

        for i, num in enumerate(nums):

            if num not in numMap:
                numMap[num] = 0

            numMap[num] += 1

        if k >= len(numMap):
            return list(numMap)

        sortedMap = sorted(numMap.items(),key = lambda item: item[1], reverse=True)

        for i in range(k):
            res.append(sortedMap[i][0])


        return res
        




            


