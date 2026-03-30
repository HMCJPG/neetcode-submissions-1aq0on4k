class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        total = 0
        prefix = [0] * len(nums)
        for i, num in enumerate(nums):
            total += num
            prefix[i] = total


        hits = 0
        freq = {}   # empty prefix
        freq[0] = 1

        for p in prefix:
            need = p - k

            if need in freq:
                hits += freq[need]

            freq[p] = freq.get(p, 0) + 1

        return hits