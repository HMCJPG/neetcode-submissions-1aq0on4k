class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort(key = lambda x : x[0])
        n = len(intervals)

        res = []
        start = 0
        skipper = 0

        res = [intervals[0]]

        for current in intervals[1:]:

            last = res[-1]
            if current[0] <= last[1]:
                # Overlap: merge!
                last[1] = max(last[1], current[1])
            else:
                # No overlap: just add it
                res.append(current)
        return res
        







