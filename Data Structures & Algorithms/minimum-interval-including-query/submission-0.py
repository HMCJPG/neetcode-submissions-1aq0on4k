class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        res = []

        for q in queries:

            min_len = float('inf')

            for left, right in intervals:
                if left <= q <= right:
                    min_len = min(min_len, right - left + 1)

            res.append(min_len if min_len != float('inf') else -1)

        return res