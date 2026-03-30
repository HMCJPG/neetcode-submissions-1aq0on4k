from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counted = Counter(nums)

        threshold = n / 3
        
        res = []

        for pair in counted.items():
            num, count = pair

            if count > threshold:
                res.append(num)

        return res