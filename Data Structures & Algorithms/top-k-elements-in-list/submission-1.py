from collections import defaultdict
# from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        seen = defaultdict(int)

        for num in nums:
            seen[num]+=1

        sortedSeen = sorted(seen.items(), key = lambda x:x[1], reverse = True)

        finale = []
        for item in sortedSeen[:k]:
            finale.append(item[0])

        return finale