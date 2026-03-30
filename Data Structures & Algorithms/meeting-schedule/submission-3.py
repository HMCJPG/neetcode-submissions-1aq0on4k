"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:


        intervals.sort(key = lambda x: x.end)

        if not intervals:
            return True

        count = 0

        finish = intervals[0].end

        

        for i in range(1, len(intervals)):

            start = intervals[i].start
            newFinish = intervals[i].end

            if start < finish:
                return False

            else:
                finish = newFinish

        return True

            








