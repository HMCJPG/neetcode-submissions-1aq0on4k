from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counted = Counter(nums)

        return max(counted, key = counted.get)