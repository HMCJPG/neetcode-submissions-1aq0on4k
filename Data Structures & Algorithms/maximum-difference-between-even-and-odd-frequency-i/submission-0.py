from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        

        sMap = Counter(s)

        max_odd = max(freq for freq in sMap.values() if freq % 2 == 1)
        min_even = min(freq for freq in sMap.values() if freq % 2 == 0)

        return max_odd - min_even