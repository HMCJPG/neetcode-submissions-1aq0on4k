class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort(key = lambda x:x[0])
        merged = []
        merged.append(intervals[0])

        for current in intervals[1:]:

            prev = merged[-1]

            if current[0] <= prev[1]:

                prev[1] = max(current[1], prev[1])

            else:
                merged.append(current)

        return merged